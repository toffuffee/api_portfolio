from waitress import serve
from templates_view.home_view import HomeView
from templates_view.contact_us_view import ContactUsView
from render_template import render_template
from templates_view.contast_us2_view import ContactUs2View
from serve_file import serve_static_file
from json_obj.get_json import GetProducts
import mimetypes

urls = {
    '/': HomeView,
    '/contact': ContactUsView,
    '/contact/2': ContactUs2View,
    '/api/products': GetProducts,
}

def app(environ, start_response):
    path = environ.get("PATH_INFO")
    print(path)
    response = serve_static_file(path, start_response)
    if response:
        return response
    view_class = urls.get(path)
    if view_class:
        view_instance = view_class()
        data = view_instance.get(environ)
        data = data.encode("utf-8")
    else:
        data = render_template(template_name='templates/404.html', context={})
        data = data.encode("utf-8")
    mime_type, encoding = mimetypes.guess_type(path)
    content_type = mime_type if mime_type else 'text/html'
    if encoding:
        content_type += f'; charset={encoding}'
    start_response(
        f"200 OK", [
            ("Content-type", content_type),
        ]
    )
    return iter([data])
serve(app)
