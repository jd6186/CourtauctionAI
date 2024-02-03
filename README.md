# CourtauctionAI
* 부동산 구매 시 참고가 되는 아파트 찾기 AI Chatbot
* 데이터 출처가 불분명해 상업적으로 이용 시 불이익이 발생할 수 있음을 미리 고지합니다.
* 기타 부가 정보는 노션 참고 : https://www.notion.so/AI-Chatbot-1855bdec7e57446e8ade57db8d01de40

## 1. 기획
1. 서비스 제작 의도 : 자신의 OpenAI API Key만 있다면 어디서든 부동산 관련 정보를 질문하고 답할 수 있는 Chatbot 생성
2. 기본 구조: RAG 구조를 활용한 Chatbot을 구현하고 이를 REST API 서버로 구현 및 간단한 UI 제작
3. 핵심 목표 : 
    - 부동산 데이터를 활용해 현재 내 자본을 입력하면 구매 가능한 서울, 경기 지역 데이터를 조회할 수 있는 기능 제작
    - 구매 추천 가격, 구매 시 주의사항 등을 고지해주는 기능 제작
4. 부가 목표 :
    - 가능하다면 현재 내 자본 입력 시 입찰 가능한 경매 목록까지 조회되도록 조회
    - 입찰 추천 가격, 입찰 시 확인할 체크리스트 검증, 주의사항 고지하는 기능 제작


## 2. 데이터 출처
1. 관련 데이터는 한국 부동산 **[국토교통부 실거래가정보 Open API](https://data.go.kr/dataset/3050988/openapi.do)를 활용해 데이터를 수집**
    - 아파트 실거래가 : [https://www.data.go.kr/data/15057511/openapi.do](https://www.data.go.kr/data/15057511/openapi.do)
    - 아파트 전월세 자료 : [https://www.data.go.kr/data/15058017/openapi.do](https://www.data.go.kr/data/15058017/openapi.do)


## 3. UI 화면 구성
1. Streamlit 라이브러리를 활용해 UI 구현
2. 공식 사이트 : [Streamlit • A faster way to build and share data apps](https://streamlit.io/)


## 4. 배포 환경 구성
1. Streamlit 라이브러리를 활용해 배포 환경 구현
2. local 실행방법 : `streamlit run streamlit_refer.py`
3. Streamlit 특성 상 소스코드 변경 시 Reboot 버튼을 클릭해 새롭게 배포해야함
