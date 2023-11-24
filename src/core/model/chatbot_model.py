import os

from langchain.document_loaders import CSVLoader, TextLoader, Docx2txtLoader, PyPDFLoader
# log
from loguru import logger

# LangChain LLM Model > OpenAI 사용
from langchain.chat_models import ChatOpenAI

# Document Loader
# from src.core.model.document_loader import load_router

# LangChain Spliter
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken # token 단위로 Splitting

# LangChain Embedding
from langchain.embeddings import HuggingFaceEmbeddings

# LangChain VectorDB
from langchain.vectorstores.chroma import Chroma

# LangChain Retrival Chain
from langchain.chains import ConversationalRetrievalChain # 메모리를 가진다는 것이 특징으로 대화를 몇개까지 저장하고 이를 활용해 검색을 하게 된다.
from langchain.memory import ConversationBufferMemory # 데이터를 몇개 저장할지 결정하는 버퍼


documents = []
base_path = "./documents"

class OpenAiModel():
    vector_db = None
    conversation_chain = None
    document_list = []

    def __init__(self):
        self.__load_default_document_list()
        chunk_list = self.__split_document()
        self.__embed_data(chunk_list)

    def __get_loader_by_file_path(self, file_name: str):
        logger.info(f'load file path : {file_name}')
        if '.csv' in file_name:
            loader = CSVLoader(file_name, encoding='utf-8')
        elif '.txt' in file_name:
            loader = TextLoader(file_name, encoding='utf-8')
        elif '.docx' in file_name:
            loader = Docx2txtLoader(file_name)
        elif '.pdf' in file_name:
            loader = PyPDFLoader(file_name)
        else:
            raise Exception('지원하지 않는 파일 형식입니다.')
        return loader

    def __get_loader_by_file_object(self, uploaded_file):
        logger.info(f'load file object : {uploaded_file}')
        file_path = base_path + "/" + uploaded_file.name
        # 파일 존재 여부 확인
        if os.path.exists(file_path):
            raise Exception(f'File already found: {file_path}')

        # 임시 파일에 내용 쓰기
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())

        # 임시 파일을 사용해서 로딩 작업 수행
        return self.__get_loader_by_file_path(file_path)

    def __load_default_document_list(self):
        result_list = []
        file_names = os.listdir(base_path)
        for file_name in file_names:
            file_name = base_path + '/' + file_name
            loader = self.__get_loader_by_file_path(file_name)
            result_list.extend(loader.load_and_split())
        self.document_list = result_list

    def __tiktoken_len(self, document):
        tokenizer = tiktoken.get_encoding("cl100k_base") # openai 기반
        return len(tokenizer.encode(document))

    def __split_document(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=100, length_function=self.__tiktoken_len)
        return text_splitter.split_documents(self.document_list)

    def __embed_data(self, chunk_list: list):
        persist_directory = 'db'
        embedding = HuggingFaceEmbeddings(
            model_name="jhgan/ko-sroberta-multitask",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )
        self.vectordb = Chroma.from_documents(
            documents=chunk_list,
            embedding=embedding,
            persist_directory=persist_directory
        )

    def __make_conversation_chain(self, openai_api_key: str):
        llm = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo", temperature=0) # GPT 3.5 터보 사용
        self.conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            chain_type="stuff", # stuff 모드로 실행 > 쿼리 그대로 1회 질문
            retriever=self.vectordb.as_retriever(search_type="mmr", vervose=True), # mmr 모드로 실행하며 출력 과정을 로깅하겠다
            memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key="answer"), # 답변에 해당하는 부분만 히스토리에 담겠다는 뜻
            get_chat_history=lambda h: h, # 메모리가 들어온 그대로 쳇 히스토리에 넣겠다
            return_source_documents=True, # llm이 참조한 문서 출력
            verbose=True, # 출력 과정을 로깅하겠다
        )

    def load_file_list(self, uploaded_file_list: list):
        for uploaded_file in uploaded_file_list:
            upload_file_name = uploaded_file.name
            if upload_file_name in documents:
                pass
            documents.append(upload_file_name)
            print(f"uploaded_file object : {uploaded_file}")
            loader = self.__get_loader_by_file_object(uploaded_file)
            self.document_list.extend(loader.load_and_split())
            chunk_list = self.__split_document()
            self.__embed_data(chunk_list)

    def get_conversation_chain(self, openai_api_key: str):
        self.__make_conversation_chain(openai_api_key)
        return self.conversation_chain
