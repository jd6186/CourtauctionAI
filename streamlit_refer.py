import os
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.core.agent.electricity_agent import ElectricityAgent
from src.core.model.chatbot_model import OpenAiModel

# ####################################### Streamlit UI 제작 ##########################################
st.set_page_config(
    page_title="CourtauctionAI",
    page_icon="🐢",
)
st.title("CourtauctionAI 🐢")
with st.sidebar:
    uploaded_file_list = st.file_uploader("Upload a file", type=["pdf", "docx", "txt", "csv"], accept_multiple_files=True)
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    process = st.button("적용")


# ######################################### Streamlit Session #########################################
# TODO - 아래 openai_api_key 부분은 삭제 필요
OPENAI_API_KEY = "..."
openai_api_key = OPENAI_API_KEY
# openai_api_key = os.getenv("OPENAI_API_KEY")
chat_model = OpenAiModel()
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Messages가 session_state 내 없을 경우
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "안녕하세요! 저는 CourtauctionAI 입니다. 어떤 도움이 필요하신가요?"}]

# 화면내 전체 Messages 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ######################################### Streamlit Button #########################################
if process:
    if not openai_api_key:
        st.info("Please enter your OpenAI API Key")
        st.stop()
    conversation_chain = chat_model.get_conversation_chain(openai_api_key)
    st.session_state.conversation = ElectricityAgent(OPENAI_API_KEY, [1000000001, 1000000002])
    if uploaded_file_list and len(uploaded_file_list) > 0:
        chat_model.load_file_list(uploaded_file_list)


# ################################################# Streamlit Chat ####################################################
def user_chat(query: str):
    # 유저가 입력한 채팅을 채팅에 저장
    st.session_state.messages.append({"role": "user", "content": query})
    # 유저가 입력한 채팅을 화면에 표출
    with st.chat_message("user"):
        st.markdown(query)


def assistant_chat(query: str):
    if not st.session_state.conversation:
        st.info("적용 버튼을 눌러 유저정보를 초기화 해주세요.")
        st.stop()
    # 응답 값 출력
    with st.chat_message("assistant"):
        agent = st.session_state.conversation
        with st.spinner("답변을 생성중입니다..."):
            # 유저 질문 질의
            # result = chain({"question": query})
            result = agent.run_question(query)
            print(f"result : {result}")
            with get_openai_callback() as cb:
                st.session_state.chat_history.append(result)
            # 응답 결과 출력
            response = result
            st.markdown(response)
            # 참고 문서 확인
            # with st.expander("참고 문서 확인"):
            #     source_documents = result
            #     for document in source_documents:
            #         st.markdown(document.metadata['source'], help=document.page_content)
    # 응답 결과 저장
    st.session_state.messages.append({"role": "assistant", "content": response})


if query := st.chat_input("질문을 입력해주세요."):
    user_chat(query)
    assistant_chat(query)


