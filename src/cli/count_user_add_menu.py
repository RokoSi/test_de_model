from typing import Union, Any

from get_user import get_users_url
from producer import get_msg_json
from settings import Settings
from validators import validator_pass


def count_user_add_menu(url: str, count_user: int = 0) -> bool:
    """
    Корректно передаеет вводимые данные для добавления пользователя
    :param url:
    :param count_user:

    :return: Ture - если пользователь успешно добавлен,
    False - если не удалось добавить пользователя
    """
    while True:
        try:
            if count_user == 0:
                count_user = int(input("введите количество пользователей: "))
            json_result: Union[list[dict[Any, Any]], bool] = get_users_url(
                 url,count_user
            )
            for user in json_result:
                valid_pass = validator_pass(user["login"]["password"])
                user["valid"] = valid_pass
                get_msg_json(user)
            return True

        except TypeError as te:
            print(f"{te}")
            return False
        except ValueError as ve:
            print(f"{ve}")
            print("введите число")
