from pprint import pprint
from typing import Union, Any

from src.get_user import get_users_url
from src.producer import get_msg_json
from src.settings import Settings
from src.validators import validator_pass


def count_user_add_menu(settings: Settings) -> bool:
    """
    Корректно передаеет вводимые данные для добавления пользователя
    :param settings: Данные для подключения к бд
    :return: Ture - если пользователь успешно добавлен,
    False - если не удалось добавить пользователя
    """
    while True:
        try:
            count_user: int = int(input("введите количество пользователей: "))
            json_result: Union[list[dict[Any, Any]], bool] = get_users_url(
                count_user, settings
            )
            if isinstance(json_result, list):
                valid_pass = validator_pass(json_result[0]['login']['password'])
                json_result[0]['valid'] = valid_pass
                get_msg_json(json_result)
                return True
            else:
                print("Не удалось получить данные")
                return False
        except TypeError as te:
            print(f"{te}")
            return False
        except ValueError as ve:
            print(f"{ve}")
            print("введите число")
