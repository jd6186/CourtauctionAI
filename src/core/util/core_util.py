import string
from datetime import datetime, timedelta, timezone
import hashlib
import random


def get_seoul_time():
    return datetime.now(timezone(timedelta(hours=9)))


def get_seoul_date_format():
    return "{:%Y-%m-%d}".format(get_seoul_time())


def get_datetime_format(datetime: datetime):
    return "{:%Y-%m-%d %H:%M:%S}".format(datetime)


def get_seoul_time_no_spaces_format():
    return "{:%Y%m%d%H%M%S}".format(get_seoul_time())


def get_seoul_datetime_format():
    return "{:%Y-%m-%d %H:%M:%S}".format(get_seoul_time())


def get_gt_seoul_datetime_format():
    return "{:%Y-%m-%d}".format(get_seoul_time()) + " 00:00:00"


def get_lt_seoul_datetime_format():
    return "{:%Y-%m-%d}".format(get_seoul_time()+timedelta(days=1)) + " 23:59:59"


def get_now_date_no_spaces_format():
    return "{:%Y%m%d}".format(get_seoul_time())


def get_now_datetime_no_spaces_format():
    return "{:%Y%m%d%H}".format(get_seoul_time()) + "0000"


def get_gt_datetime_no_spaces_format():
    return "{:%Y%m%d%H}".format(get_seoul_time()-timedelta(hours=24)) + "0000"


def get_lt_datetime_no_spaces_format():
    return "{:%Y%m%d%H}".format(get_seoul_time()-timedelta(hours=23)) + "0000"


def convertor_no_space_to_datetime(no_space_datetime: str):
    result = no_space_datetime[:4] + "-" + no_space_datetime[4:6] + "-" + no_space_datetime[6:8] + " 01:00:00"
    print(f"# convertor_no_space_to_datetime : {result}")
    return result


def hash_function(password: str) -> str:
    # 비밀번호를 바이트 형식으로 변환
    password_bytes = password.encode()

    # SHA-256 해시 생성 및 업데이트
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password_bytes)

    # 해시된 비밀번호를 16진수 형식의 문자열로 반환
    return sha256_hash.hexdigest()


def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string