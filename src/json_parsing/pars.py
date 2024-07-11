import logging
from pprint import pprint
from typing import Union, List

from .model.users import Users

log = logging.getLogger(__name__)


def pars_user(dict_param: list) -> Union[List[Users], bool]:
    print("var 1")
    print(dict_param)
    print(type(dict_param))
    """
    Парсинг полученного dict.
    :param dict_param: json приведенный к dict
    :return: Users - если удалось распарить | bool - если не удалось распарсить
    """
    try:
        users: List[Users] = [Users(**user) for user in dict_param]
        print("var 2")
        print(users)
        return users
    except (TypeError, KeyError, ValueError) as e:
        log.error(f"Ошибка {e}")
        return False
