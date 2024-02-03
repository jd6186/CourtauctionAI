# coding: utf-8

from sqlalchemy import BigInteger, Column, DateTime, String, Text, text, Date
from src.core.database.database import Base


class User(Base):
    __tablename__ = 'tb_user'

    user_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='유저 고유번호')
    login_id = Column(String(100), nullable=False, comment='로그인 이메일 계정', unique=True)
    hashed_password = Column(String(1000), nullable=False, comment='로그인 패스워드 해쉬값')
    last_login_datetime = Column(DateTime, comment='마지막 로그인 일자')
    created_datetime = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='생성일시')
    modified_datetime = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='수정일시')
    password_update_datetime = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False,
                                      comment='패스워드 마지막 변경 일자')
    user_name = Column(String(100), nullable=False, comment='유저명')
    nickname = Column(String(100), nullable=False, comment='유저 닉네임')
    user_key = Column(String(1000), nullable=False, comment='유저 OpenAI 고유번호 키값')


class UserWithdrawalHistory(Base):
    __tablename__ = 'tb_user_withdrawal_history'

    withdrawal_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='탈퇴 이력 고유번호')
    withdrawal_datetime = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='탈퇴 일시')
    withdrawal_reason = Column(String(1000), nullable=False, comment='탈퇴 사유')
    user_id = Column(BigInteger, nullable=False, comment='유저 고유번호')
    login_id = Column(String(100), nullable=False, comment='로그인 이메일 계정')
    hashed_password = Column(String(1000), nullable=False, comment='로그인 패스워드 해쉬값')
    last_login_datetime = Column(DateTime, comment='마지막 로그인 일자')
    created_datetime = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='생성일시')
    modified_datetime = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='수정일시')
    password_update_datetime = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False,
                                      comment='패스워드 마지막 변경 일자')
    user_name = Column(String(100), nullable=False, comment='유저명')
    nickname = Column(String(100), nullable=False, comment='유저 닉네임')
    user_key = Column(String(1000), nullable=False, comment='유저 OpenAI 고유번호 키값')