
from datetime import datetime, timedelta

from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

# 환경변수에서 API 키를 가져온다.
OPENAI_API_KEY = 'sk-03h3bkFJpTeBGlDDbtNSzql1EtUs' # os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo", temperature=0)  # GPT 3.5 터보 사용

tools = [
    Tool(
        name="Datetime",
        description="I check the time.",
        func=lambda x: f"""
        오늘 : {datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
        내일 : {(datetime.now() + timedelta(days=1)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
        모레 : {(datetime.now() + timedelta(days=2)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
        모래 : {(datetime.now() + timedelta(days=2)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
        어제 : {(datetime.now() - timedelta(days=1)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
        엇그제 : {(datetime.now() - timedelta(days=2)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
        그제 : {(datetime.now() - timedelta(days=2)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
        그그제 : {(datetime.now() - timedelta(days=3)).strftime("%Y년 %m월 %d일 %H시 %M분 %S초")},
        ...
        """,
    ),
    Tool(
        name="Workplace",
        description="I check the workplace.",
        func=lambda x: f"""
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
    ),
    Tool(
        name="Electricity Data",
        description="I check the workplace.",
        func=lambda x: """
        1000000001: {'2023-11-22': '100w'}
        1000000002: {'2023-11-22': '200w'}
        1000000003: {'2023-11-22': '300w'}
        2000000001: {'2023-11-22': '400w'}
        2000000002: {'2023-11-22': '500w'}
        3000000001: {'2023-11-22': '600w'}
        """
    )
]

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)


if __name__ == "__main__":
    question = "어제 아난티코드 전기 사용량은 얼마야??"
    context = f"""
    The result for areas not found in my work_place_list is always "Not available for retrieval."\n
    my_workplace_list: [1000000002, 1000000003]\n
    Question: {question}
    """
    agent.run(
        context
    )

"""
1. 아난티 내에서도 서로 볼 수 있는 곳과 없는 곳이 존재한다.
2. 때문에 관리자의 권한 정보를 확인 필요하다.
3. MongoDB에 user 테이블을 보면 workplace_list가 존재한다.
4. workplace_list에 있는 사업장 정보를 기준으로 사용자가 입력한 장소 정보를 비교하여 조회 가능한지 여부를 파악한다.
5. 조회 가능하다면, 해당 장소의 데이터 조회한다.
6. 조회한 데이터를 기반으로 사용자가 물은 질문에 대한 내용을 분석한다.
"""
