## dummy-api

| **Метод** | **Эндпоинт**        | **Описание**                                                                                  | **Пример ответа**                                                                                                                                                              |
|-----------|---------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GET`     | `/`                 | Возвращает приветственное сообщение.                                                         | `{"message": "Welcome to the Dummy Web API!"}`                                                                                                                              |
| `GET`     | `/api/data`         | Возвращает список данных в формате JSON, обработанных с помощью `pandas`.                   | `[{"id": 1, "name": "Item 1", "description": "This is item 1"}, {"id": 2, "name": "Item 2", "description": "This is item 2"}]`                                               |
| `POST`    | `/api/data`         | Принимает JSON-данные в теле запроса и возвращает их с подтверждением.                       | `{"received_data": {"key": "value"}, "status": "success"}`                                                                                                                   |
| `GET`     | `/api/version`      | Возвращает текущую версию API.                                                               | `{"api_version": "1.0.0"}`                                                                                                                                                   |
| `GET`     | `/api/external`     | Выполняет запрос к внешнему API (`https://jsonplaceholder.typicode.com/posts/1`) и возвращает его данные. | `{"external_data": {"userId": 1, "id": 1, "title": "Sample title", "body": "Sample body"}}`                                                                                  |