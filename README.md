# REST Json Schema Generator

Сервис для генерации Pydantic-моделей, REST-эндпоинтов по JSON-schema.

# Запуск

1. Запустить PostgreSQL

```shell
make storages
```

2. Запустить приложение

```shell
make app
```

3. Swagger должен быть доступен по адресу `localhost:8000/api/docs`

4. Завершение работы

```shell
make down-all
```

# CLI

С помощью CLI можно добавлять новые модели и эндпоинты.

## Установка

Для использования CLI необходимо установить проект:

```shell
rye sync
```

Возможен способ(не проверялся):

```shell
pip install -r requirements.lock
```

## Использование

1. Проверить файлы

```shell
rest-cli check batch -i <Путь до папки с JSON-schema> -v
```

2. Добавить модели

```shell
rest-cli models batch -i <Путь до папки с JSON-schema>
```

3. Добавить ручки

```shell
rest-cli routes batch
```

Для получения полного списка параметров можно воспользоваться флагом `--help`

```shell
rest-cli --help
```

## Регистрация в проекте

При использовании параметров по-умолчанию сгенерированные файлы добавляются в:

- модели - в `src/rest_json_schema/presentation/api/schemas`
- эндпоинты - в `src/rest_json_schema/presentation/api/routes/json_schemas_rest`

Для регистрации нового эндпоинта необходимо в файл `src/rest_json_schema/presentation/api/routes/json_schemas_rest/register.py` добавить новый `route`

### Пример регистрации

Было:

```python
...
from . import format, specific_format
...
    routers: list[APIRouter] = [
        format.router,
        specific_format.router,
    ]
...
```

Стало:

```python
...
from . import format, specific_format, new_route  <---- Новый импорт
...
    routers: list[APIRouter] = [
        format.router,
        specific_format.router,
        new_route.router,  <---- Регистрация
    ]
...
```

# Формат JSON-schema

Пример исходного файла можно найти в `static`:

- `static/format.json`
- `static/specific_format.json`

Допускается добавлять новые параметры или изменять качественные характеристики исходных.
Нельзя изменять имена существующих параметров.
Зарезервированные названия: Root, Specification, Configuration, Settings.

Основная задумка программы - возможность изменять схему параметров Specification, Settings

# Тестирование

Для тестирования используется `pytest`

- Запуск тестов

```shell
rye test
```

- Альтернативный запуск тестов

```shell
pytest
```

# Линтеры

В качестве линтера и форматтера используется ruff

```shell
rye lint
```

```shell
rye format
```

# Makefile commands

- `app` - Запустить контейнеры-приложение
- `storages` - Запустить контейнеры-хранилища
- `down-app` - Закрыть контейнеры-приложение
- `down-storages` - Закрыть контейнеры-хранилища
- `down-storages-v` - Удалить сохраненные данные хранилищ
- `down-all` - Закрыть все запущенные контейнеры

# Стек

- Python3.11
- FastAPI
- SQLAlchemy
- typer
- datamodel_code_generator
- PostgreSQL
- alembic
- dishka
- Docker
- pydantic
- poetry
