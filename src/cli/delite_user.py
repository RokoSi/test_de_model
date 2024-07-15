from src.settings import Settings
from src.validators.validator_email import validator_email


def delite_user(settings: Settings) -> None:
    """
    Удаление пользователя по email, если он валиден
    :param settings: Данные для подключения к бд
    """
    while True:
        email: str = str(input("введите email: "))
        if validator_email(email):
            check_del = True
            if check_del:
                print("Пользовать удален\n")
                break
            else:
                print("Нет такого пользователя")
                break
        else:
            print("введите валидный пароль")
