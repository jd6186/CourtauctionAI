# 기본 이미지로부터 빌드 시작
FROM python:3.9-slim
USER root

# 애플리케이션 복사
COPY /env /env
COPY /src /src
COPY requirements.txt requirements.txt
COPY main.py main.py

# 환경변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENV=local

# 필요한 패키지 설치
RUN apt-get update && apt-get -y upgrade \
  && apt-get install -y gcc \
  && apt-get -y clean \
  && rm -rf /var/lib/apt/lists/*

# 파이썬 라이브러리 설치
RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt

# 애플리케이션 실행
CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:8000"]
