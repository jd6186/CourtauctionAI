from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI

from src.core.template.base import get_base_template
from src.core.template.resort import get_tools


# 환경변수에서 API 키를 가져온다.
class ElectricityAgent():
    def __init__(self, openai_api_key, my_workplace_list):
        self.tools = get_tools(openai_api_key)
        llm = ChatOpenAI(openai_api_key=openai_api_key, max_tokens=2000, temperature=0)
        self.agent = initialize_agent(
            self.tools
            , llm
            , agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
            , verbose=True
            , handle_parsing_errors=True
        )
        self.my_workplace_list = my_workplace_list

    def run_question(self, query: str):
        print("Check ######################################################")
        context = get_base_template(query, self.my_workplace_list)
        return self.agent.run(context)
