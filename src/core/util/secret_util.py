import os
import json
from dotenv import load_dotenv, find_dotenv


def get_secret_data():
    env = os.environ.get('ENV')
    dotenv_path = "env/.env.local"
    if env:
        dotenv_path = 'env/.env.' + str(env)
    load_dotenv(find_dotenv(dotenv_path))
    secret_data = os.environ.get('SECRET_DATA')
    if secret_data:
        return json.loads(secret_data)

