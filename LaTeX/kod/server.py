"""
# Документация приложения

## Обзор
Это приложение на языке Python служит веб-сервером с использованием фреймворка Waitress. 
Он обрабатывает различные URL-маршруты для отображения HTML-шаблонов, обслуживания 
статических файлов и предоставления конечных точек API. Приложение поддерживает такие 
функции, как загрузка изображений, аутентификация пользователя и административные 
функциональности.

## Зависимости
- Python 3.x
- Waitress
- cgi
- mimetypes

## Структура файлов
- `templates_view/`: Каталог, содержащий различные классы представлений для отображения HTML-шаблонов.
- `render_template.py`: Модуль для отображения HTML-шаблонов.
- `serve_file.py`: (Добавьте описание для модуля serve_file.py, если он существует)
- `json_obj/`: Каталог для модулей, отвечающих за обработку JSON-объектов.
- `db_info/`: Каталог для модулей, отвечающих за взаимодействие с базой данных.

## Маршруты URL
- `/`: Главная страница (HomeView)
- `/image/`: Просмотр изображений (ImageView)
- `/admin/login`: Вход в админ-панель (AdminLogin)
- `/api/images`: Получение изображений через API (GetImages)
- `/admin`: Админ-панель (AdminView)
- `/api/login`: Аутентификация администратора через API (GetAdmin)
- `/api/upload_image`: Загрузка изображений через API (метод POST)

## Запуск приложения
Для запуска приложения выполнить скрипт `server.py`:
```bash
python server.py
"""

import cgi
from waitress import serve
from templates_view.home_view import HomeView
from templates_view.image_view import ImageView
from templates_view.admin_login import AdminLogin
from templates_view.admin import AdminView
from render_template import render_template
from serve_file import serve_static_file
from json_obj.get_images import GetImages
from db_info.connect import insert_image_to_db
from json_obj.get_admin import GetAdmin
import mimetypes

urls = {
    '/': HomeView,
    '/image/': ImageView,
    '/admin/login': AdminLogin,
    '/api/images': GetImages,
    '/admin': AdminView,
    '/api/login': GetAdmin
}

def app(environ, start_response):
    path = environ.get("PATH_INFO")
    if environ['REQUEST_METHOD'] == 'POST':
        if path == '/api/upload_image':
            form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
            image_data = form['image'].file.read()
            image_name = form.getvalue('image_name', '')
            image_desc = form.getvalue('image_desc', '')
            image_country = form.getvalue('image_country', '')
            insert_image_to_db(image_data,image_name, image_desc, image_country)
            start_response("200 OK", [("Content-type", "application/json")])
            return [b'{"status": "success"}']

    if path.startswith("/image/") and "/image/" in urls:
        view_class = urls["/image/"]
    else:
        view_class = urls.get(path)
    if view_class:
        view_instance = view_class()
        data = view_instance.get(environ)
        data = data.encode("utf-8")
    else:
        response = serve_static_file(path, start_response)
        if response:
            return response
        data = render_template(template_name='templates/404.html')
        data = data.encode("utf-8")

    mime_type, encoding = mimetypes.guess_type(path)
    content_type = mime_type if mime_type else 'text/html'
    if encoding:
        content_type += f'; charset={encoding}'
    start_response("200 OK", [("Content-type", content_type)])
    return iter([data])

if __name__ == "__main__":
    serve(app)
