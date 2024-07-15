# Тестовый проект для DE (1-st step)

[Задание](./TODO.md)

> Для тестовой среды рекомендуется использовать `docker-compose.yml`

> Тестовые переменные в файле `.env.dev`

Ниже описать реализацию и документацию к коду
___

- **Python**
- **Git**
- **Docker**
- **PostgreSQL**

# Проект: Интерфейс для взаимодействия с API и хранения пользователей в БД

## Описание

Это новая версия проекта, которая служит для обучения передавать и принимать сообщения с помощью kafka.
Это 1 часть приложения, где я реализовал Producer`a.

## Функциональность

- Получение данных о пользователях из API
- Проверка валидности email
- Проверка сложности паролей
- отправка сообщения

## Установка и запуск

### Установка зависимостей

Используйте Poetry для установки всех зависимостей:

```bash
poetry install
```

После запуска проекта, в консоль выведется меню:

```
Меню:
1. Добавить пользователей
2. Получить валидных пользователей
3. Получить невалидных пользователей
4. Проверить наличие email
5. Изменение данных
6. Выйти
Выберите пункт меню: 
```

Важно! Вводить нужно числа, но в программе предусмотрена обработка ошибок.

#### Рассмотрим подробнее каждый раздел.

### Добавить пользователей

В этом разделе необходимо будет выбрать, какое количество пользователей нужно добавить в БД.

```
Меню:
1. Добавить пользователей
2. Получить валидных пользователей
3. Получить невалидных пользователей
4. Проверить наличие email
5. Изменение данных
6. Выйти
Выберите пункт меню: 1
введите количество пользователей: 1
```

После получения пользователей, будет выведена вся полученная информация и сохранена в БД.
Например:

```
{'info': {'page': 1,
          'results': 1,
          'seed': '9326d3b7e714e495',
          'version': '1.4'},
 'results': [{'cell': '(692) 407 1998',
              'dob': {'age': 34, 'date': '1990-05-24T23:25:42.193Z'},
              'email': 'claudio.yanez@example.com',
              'gender': 'male',
              'id': {'name': 'NSS', 'value': '08 12 77 9082 6'},
              'location': {'city': 'Ochomitas',
                           'coordinates': {'latitude': '23.9221',
                                           'longitude': '-110.6651'},
                           'country': 'Mexico',
                           'postcode': 43765,
                           'state': 'Campeche',
                           'street': {'name': 'Corredor Vietman',
                                      'number': 3385},
                           'timezone': {'description': 'Almaty, Dhaka, Colombo',
                                        'offset': '+6:00'}},
              'login': {'md5': '711109eaed466cbbde188c7590f98fd5',
                        'password': '1230',
                        'salt': 'w4CuClLp',
                        'sha1': '284b69f8264d9301b92f03005710d0b9166f864e',
                        'sha256': '63b8dc37e764a7c1c8f5a106e433c7216816e9b323502654b525926a98ca9cf5',
                        'username': 'crazybear162',
                        'uuid': '2fc58816-5e75-4729-8040-1c1971457b0d'},
              'name': {'first': 'Claudio', 'last': 'Yáñez', 'title': 'Mr'},
              'nat': 'MX',
              'phone': '(641) 234 7083',
              'picture': {'large': 'https://randomuser.me/api/portraits/men/60.jpg',
                          'medium': 'https://randomuser.me/api/portraits/med/men/60.jpg',
                          'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/60.jpg'},
              'registered': {'age': 19, 'date': '2004-08-21T06:38:48.436Z'}},
              'valid': False]}
```

### Важно №1!

Обратим внимание на последнее поле:

```
'valid': False
```

Это дополнительно поле, которые информирует о валидности пароля

### Важно №2!

Программа выведет успешное количество добавленных пользователей в БД.

``` 
Успешно добавлено:  1 записей
```

Если программа установленна корректно, то причиной не добавления записи в БД, может служить ограничения на атрибуты "
city, state, country", так как их комбинация является уникальной.
Дополнительно идет проверка на валидность пароля, если пароль валиден, то в атрибут "password_validation", будет записан
True, иначе False.

Условия на валидный пароль:

```
upper      ABCDEFGHIJKLMNOPQRSTUVWXYZ
lower      abcdefghijklmnopqrstuvwxyz
number     0123456789
special    !"#$%&'()*+,- ./:;<=>?@[\]^_`{|}~
```

### Добавить пользователей

Данный раздел выводит всех пользователей в БД, у кого валидный пароль, если нет, то будет получено сообщение:

```chatinput
нет таких записей
```

### Получить невалидных пользователей

Данный раздел выводит всех пользователей в БД, у кого не валидный пароль, если нет, то будет получено сообщение:

```chatinput
нет таких записей
```

### Проверить наличие email

Данный раздел проверяет, если ли такой email в БД.

Пример:

```
Меню:
1. Добавить пользователей
2. Получить валидных пользователей
3. Получить невалидных пользователей
4. Проверить наличие email
5. Изменение данных
6. Выйти
Выберите пункт меню: 4
введите email:mathis.gauthier@example.com
есть такой email в базе
 ```

В случаи когда пользователя нет в БД будет получено сообщение:

```chatinput
Выберите пункт меню: 4
введите email:athis.gauthir@example.com
нет такого email в базе
```

### Изменение данных

Данный раздел предлагает изменить данные пользователя, выбор пользователя осуществляется по email.

```chatinput
Меню:
1. Добавить пользователей
2. Получить валидных пользователей
3. Получить невалидных пользователей
4. Проверить наличие email
5. Изменение данных
6. Выйти
Выберите пункт меню: 5
1. city
2. state
3. country
4. phone
5. cell
6. street_name
7. street_number
8. postcode
9. latitude
10. longitude
11. picture
12. email
13. username
14. password
15. password_md5
16. gender
17. name_title
18. name_first
19. name_last
20. age
21. nat
выберите параметр на изменение:
```

Необходимо ввести цифру параметра, который нужно изменить:

```chatinput
выберите параметр на изменение:1
Вы выбрали параметр: city
На что поменять: Rostov-on-Don
```

### Выйти

Пункт отвечает за то, что вы выходите из программы.