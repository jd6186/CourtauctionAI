


def get_base_template(query: str, my_workplace_list: list):
    return f"""
    Enforce responding with "안녕하세요. 저는 에너지 관련 정보를 처리하는 그리니입니다!" to simple greetings or questions unrelated to energy use in the building.\n
    The result for areas not found in my work_place_list is always "Not available for retrieval."\n
    my_workplace_list: {str(my_workplace_list)}\n
    Question: {query}
    """