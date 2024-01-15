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
    print(path)

    if environ['REQUEST_METHOD'] == 'POST':
        if path == '/api/upload_image':
            form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)

            # Extracting image data
            image_data = form['image'].file.read()

            # Extracting other form fields
            image_name = form.getvalue('image_name', '')
            image_desc = form.getvalue('image_desc', '')
            image_country = form.getvalue('image_country', '')

            # Now you can use the extracted data
            print(image_data)
            print(image_desc)
            print(image_country)

            insert_image_to_db(image_data,image_name, image_desc, image_country)

            start_response("200 OK", [("Content-type", "application/json")])
            return [b'{"status": "success"}']

    # Далее ваш существующий код для обработки GET-запросов
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
