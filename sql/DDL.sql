create table tb_user
(
    user_id bigint auto_increment primary key comment '유저 아이디',
    login_id varchar(100) not null unique comment '로그인 아이디',
    hashed_password varchar(1000) not null comment '해시된 비밀번호',
    last_login_datetime datetime comment '마지막 로그인 시간',
    created_datetime datetime not null default CURRENT_TIMESTAMP comment '생성 시간',
    modified_datetime datetime not null default CURRENT_TIMESTAMP comment '수정 시간',
    password_update_datetime datetime not null default CURRENT_TIMESTAMP comment '비밀번호 수정 시간',
    user_name varchar(100) not null comment '유저 이름',
    nickname varchar(100) not null comment '닉네임',
    user_key varchar(1000) not null comment '유저 openai 키'
);


create table tb_user_withdrawal_history
(
    withdrawal_id bigint auto_increment primary key comment '탈퇴 아이디',
    withdrawal_datetime datetime not null default CURRENT_TIMESTAMP comment '탈퇴 시간',
    withdrawal_reason varchar(1000) not null comment '탈퇴 사유',
    user_id bigint not null comment '유저 아이디',
    login_id varchar(100) not null comment '로그인 아이디',
    hashed_password varchar(1000) not null comment '해시된 비밀번호',
    last_login_datetime datetime comment '마지막 로그인 시간',
    created_datetime datetime not null default CURRENT_TIMESTAMP comment '생성 시간',
    modified_datetime datetime not null default CURRENT_TIMESTAMP comment '수정 시간',
    password_update_datetime datetime not null default CURRENT_TIMESTAMP comment '비밀번호 수정 시간',
    user_name varchar(100) not null comment '유저 이름',
    nickname varchar(100) not null comment '닉네임',
    user_key varchar(1000) not null comment '유저 openai 키',
    constraint tb_user_withdrawal_history_tb_user_user_id_fk
        foreign key (user_id) references tb_user (user_id)
);