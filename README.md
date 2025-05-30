```markdown
# Pet Project: Notes API

## Описание

Это простое API для управления заметками, которое позволяет добавлять, редактировать и удалять заметки с заголовком и описанием. Проект построен с использованием Python, FastAPI, SQLAlchemy, Pydantic и Docker.

## Стек технологий

- Python: Основной язык программирования.
- FastAPI Фреймворк для создания API.
- SQLAlchemy ORM для работы с базой данных.
- Pydantic Для валидации данных.
- Docker Для контейнеризации приложения.
- Alembic Для миграции БД
- AuthX Для аутентификации

## Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/chinazes532/notes_api.git
   cd notes_api
   ```

2. Соберите и запустите контейнер:

   ```bash
   docker build . -t name

   docker run -it -d - -restart=unless-stopped - -name name name
   ```

3. API будет доступно по адресу: `http://localhost:8000`.

## Использование

API поддерживает следующие эндпоинты:

- **POST /notes**: Создает новую заметку.
- **GET /notes**: Получает список всех заметок.
- **GET /notes/{id}**: Получает заметку по ID.
- **PUT /notes/edit/title/{id}**: Обновляет заголовок заметки по ID.
- **PUT /notes/edit/desc/{id}**: Обновляет описание заметки по ID.
- **DELETE /notes/delete/{id}**: Удаляет заметку по ID.

### Пример запроса на создание заметки:

```json
{
  "title": "Заголовок заметки",
  "description": "Описание заметки"
}
```

