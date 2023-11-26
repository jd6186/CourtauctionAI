from datetime import datetime, timedelta

from langchain.chains import ConversationalRetrievalChain
from langchain.tools import Tool

from src.core.model.chatbot_model import OpenAiModel

template_datetime = f"""
오늘 : {datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
내일 : {(datetime.now() + timedelta(days=1)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
모레 : {(datetime.now() + timedelta(days=2)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
모래 : {(datetime.now() + timedelta(days=2)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
어제 : {(datetime.now() - timedelta(days=1)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
엇그제 : {(datetime.now() - timedelta(days=2)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
그제 : {(datetime.now() - timedelta(days=2)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
그그제 : {(datetime.now() - timedelta(days=3)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
...
"""

template_workplace = f"""
아난티: 1000000000
    코드: 1000000001
    부산: 1000000002
    서울: 1000000003
코오롱: 2000000000
    마곡: 2000000001
    과천: 2000000002
메가존: 3000000000
    과천: 3000000001
"""

template_electricity_data = """
1000000001: {'2023-11-22': '100w'}
1000000002: {'2023-11-22': '200w'}
1000000003: {'2023-11-22': '300w'}
2000000001: {'2023-11-22': '400w'}
2000000002: {'2023-11-22': '500w'}
3000000001: {'2023-11-22': '600w'}
"""

template_nothing_to_say = """
a proper greeting
"""


def get_tools(openai_api_key: str):
    chain = OpenAiModel().get_conversation_chain(openai_api_key)
    return [
        Tool(
            name="Greetings",
            description="Look at the question and make up the appropriate words yourself.",
            func=lambda x: template_nothing_to_say
        ),
        Tool(
            name="Datetime",
            description="I check the time.",
            func=lambda x: template_datetime
        ),
        Tool(
            name="Workplace",
            description="I check the workplace.",
            func=lambda x: template_workplace
        ),
        Tool(
            name="Electricity Data",
            description="I check the workplace.",
            func=lambda x: template_electricity_data
        ),
        Tool(
            name="Use this for questions that are difficult to answer",
            func=chain.run,
            description="useful for when you need to answer questions about LLM",
            return_direct=True,
        )
    ]
