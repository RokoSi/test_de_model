
from ..validators import validator_email


def check_email(settings) -> None:
    """
    Если ли пользователь в бд
    :param settings: Данные для подключения к бд
    """
    while True:
        email: str = str(input("введите email: "))
        if validator_email(email):
            if True:  # get_check_email(settings, email):
                print("Пользователь есть в бд \n")
                break
            # else:
            #     print("нет пользователя в бд")
            #     break
        else:
            print("введите валидный пароль")
