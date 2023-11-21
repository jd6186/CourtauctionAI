import streamlit as st
from langchain.memory import StreamlitChatMessageHistory
from langchain.callbacks import get_openai_callback

from src.core.model.chatbot_model import OpenAiModel


def set_default_conversation():
    st.set_page_config(
        page_title="CourtauctionAI",
        page_icon="🐢",
    )

    st.title("CourtauctionAI 🐢")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    with st.sidebar:
        uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "txt", "csv"], accept_multiple_files=True)
        openai_api_key = st.text_input("OpenAI API Key", type="password")
        process = st.button("Process")

    if process:
        if not openai_api_key:
            st.info("사용하실 OpenAI API Key를 입력해주시면 Chatbot을 사용하실 수 있습니다.")
            st.stop()
        chat_model = OpenAiModel()
        st.session_state.conversation = chat_model.get_conversation_chain(openai_api_key)

    if 'messages' not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "안녕하세요! 저는 CourtauctionAI 입니다. 어떤 도움이 필요하신가요?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    history = StreamlitChatMessageHistory(key="chat_message")
    chatting()


def chatting():
    if query := st.chat_input("질문을 입력해주세요."):
        # 유저가 입력한 채팅을 채팅에 저장
        st.session_state.messages.append({"role": "user", "content": query})

        # 유저가 입력한 채팅을 화면에 표출
        with st.chat_message("user"):
            st.markdown(query)

        # 응답 값 출력
        with st.chat_message("assistant"):
            chain = st.session_state.conversation
            with st.spinner("답변을 생성중입니다..."):
                # 유저 질문 질의
                result = chain({"question": query})
                with get_openai_callback() as cb:
                    st.session_state.chat_history = result["chat_history"]
                # 응답 결과 출력
                response = result["answer"]
                st.markdown(response)

                # 참고 문서 확인
                with st.expander("참고 문서 확인"):
                    source_documents = result["source_documents"]
                    for document in source_documents:
                        st.markdown(document.metadata['source'], help=document.page_content)

        # 응답 결과 저장
        st.session_state.messages.append({"role": "assistant", "content": response})
