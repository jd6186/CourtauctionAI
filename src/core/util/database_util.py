from fastapi import HTTPException

from sqlalchemy.orm import Session

from src.core.code.error_type_code import EXCEPTION_TYPE


def domain_save(domain, db: Session):
    db.add(domain)
    db.flush()
    db.refresh(domain)
    return domain


def domain_all_save(domain_list: list, db: Session):
    db.add_all(domain_list)
    db.flush()
    return domain_list


def domain_update(query, data):
    result = query.update(data)
    if result != 1:
        EXCEPTION_TYPE.raise_exception(EXCEPTION_TYPE.ERROR_506)


def domain_delete(query):
    result = query.delete()
    if result != 1:
        EXCEPTION_TYPE.raise_exception(EXCEPTION_TYPE.ERROR_506)


def like_search(str_val):
    return "%" + str(str_val) + "%"


def domain_list_to_dto_list(domain_list: list, dto_class):
    return [domain.to_dto(dto_class) for domain in domain_list]