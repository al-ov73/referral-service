Реферальная система с авторизацией по номеру телефона.
Пользователю при авторизации присваивается 6-значный код, который могут вводить другие пользователи.

[Коллекция в Postman](https://www.postman.com/al-ov73/workspace/public-workspace/collection/31495401-2d5aeac5-cff9-4f58-ad9d-8cc8ac1ff5be?action=share&creator=31495401)<br><br>
Описание API:

1. Создание пользователя
POST http://127.0.0.1:8000/api/v1/auth/users/
В body следует указать поля "phone" и "password"
<br><br>
2. Аутентификация пользователя<br>
POST http://127.0.0.1:8000/auth/token/login/ <br>
В body следует указать поля "phone" и "password"
В Response вернется JSON-строка с токеном
```commandline
{
    "auth_token": "2740cfe ... 3ffd6a8"
}
```

3. Страница профиля<br>
GET http://127.0.0.1:8000/api/v1/users/<id_профиля> <br>
В headers запроса необходимо указать поле
```commandline
Authorization = Token 2740cfeb0...68083ffd6a8
```
для получения данных о пользователе
пример информации о пользователе:
```commandline
{
    "id": 1,
    "phone": "+79991111111",
    "ref_code": "6lyt5Cs7",
    "ref_received": [
        5
    ],
    "ref_active": false
}
```

4. Отправка реферального кода другого пользователя<br>
POST http://127.0.0.1:8000/api/v1/users/<id_профиля>/send_ref <br>
id пользователя, который отпавил код, привязывается к профилю полуателя в поле "ref_received"