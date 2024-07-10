from pprint import pprint
from typing import Union, Any, List

#from src.db_use.save_user import save_user
from src.json_parsing import get_users_url, pars_user
from src.json_parsing.model.users import Users
from src.ka_ca import get_msg_json
#from src.ka_ca import get_msg_json
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
                users_result: Union[List[Users], bool] = pars_user(json_result)
                if isinstance(users_result, list):
                    for user in users_result:
                        pprint(user)
                        valid_pass: bool = validator_pass(user.login.password)
                        if not get_msg_json(settings, user, valid_pass):               #!!!!!!
                            print("Не получилось добавить пользователя")
                            return False
                        else:
                            print("Пользователь успешно добавлен")
                return True
            else:
                print("Не удалось получить данные")
                return False
        except TypeError:
            return False
        except ValueError:
            print("введите число")
