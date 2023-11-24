# LangChain DocumentLoader
from langchain.document_loaders import CSVLoader, TextLoader, PyPDFLoader, Docx2txtLoader
from loguru import logger

base_file_dir = '../../../documents/'

def load_file(file_name: str):
    file_name = base_file_dir + file_name
    if '.csv' in file_name:
        loader = CSVLoader(file_name)
    elif '.txt' in file_name:
        loader = TextLoader(file_name)
    elif '.docx' in file_name:
        loader = Docx2txtLoader(file_name)
    elif '.pdf' in file_name:
        loader = PyPDFLoader(file_name)
    else:
        raise Exception('지원하지 않는 파일 형식입니다.')
    return loader.load()

