"""
# Документация для модуля serve_file.py

## Описание
Модуль `serve_file.py` предоставляет функционал для обслуживания статических файлов, включая их чтение и передачу клиенту.

## Зависимости
- Python 3.x
- mimetypes

## Функции

### serve_file(path, start_response)
Сервисная функция для обслуживания конкретного файла по заданному пути.

#### Параметры
- `path` (строка): Путь к файлу, который требуется обслужить.
- `start_response` (callable): Функция обратного вызова для установки статуса и заголовков ответа.

#### Возвращаемые значения
- Возвращает содержимое файла в виде байтового объекта.
- В случае отсутствия файла, возвращает статус "404 Not Found" с соответствующим сообщением.

### serve_static_file(path, start_response)
Функция для обслуживания статических файлов в рамках текущего приложения.

#### Параметры
- `path` (строка): Путь к файлу, который требуется обслужить.
- `start_response` (callable): Функция обратного вызова для установки статуса и заголовков ответа.

#### Возвращаемые значения
- Вызывает `serve_file` для обслуживания конкретного файла внутри директории "/src/".
"""

import mimetypes

def serve_file(path, start_response):
    """
    Сервисная функция для обслуживания конкретного файла по заданному пути.
    
    :param path: Путь к файлу, который требуется обслужить.
    :param start_response: Функция обратного вызова для установки статуса и заголовков ответа.
    :return: Содержимое файла в виде байтового объекта. В случае отсутствия файла, возвращает статус "404 Not Found" с соответствующим сообщением.
    """
    new_path = path.replace('/', '', 1)
    try:
        with open(new_path, 'rb') as f:
            content = f.read()
        mime_type, _ = mimetypes.guess_type(new_path)
        if mime_type is None:
            mime_type = 'application/octet-stream'
        start_response("200 OK", [("Content-type", mime_type)])
        return [content]
    except FileNotFoundError:
        start_response("404 Not Found", [("Content-type", "text/plain")])
        return [b"404 Not Found"]

def serve_static_file(path, start_response):
    """
    Функция для обслуживания статических файлов в рамках текущего приложения.
    
    :param path: Путь к файлу, который требуется обслужить.
    :param start_response: Функция обратного вызова для установки статуса и заголовков ответа.
    """
    if path.startswith("/src/"):
        return serve_file(path, start_response)
