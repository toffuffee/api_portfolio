from waitress import serve
from templates_view.home_view import HomeView
from templates_view.contact_us_view import ContactUsView
from render_template import render_template
from templates_view.contast_us2_view import ContactUs2View
from serve_file import serve_static_file
from json_obj.get_json import GetProducts

urls = {
    '/': HomeView,
    '/contact': ContactUsView,
    '/contact/2': ContactUs2View,
    '/api/products': GetProducts,
}
content_types = {
    '/api/': 'application/json; charset=UTF-8',
    'default': 'text/html; charset=UTF-8'
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
        content_type = content_types.get(next((key for key in content_types if path.startswith(key)), 'default'))
        data = view_instance.get(environ)
        data = data.encode("utf-8")
    else:
        data = render_template(template_name='templates/404.html', context={})
        content_type = 'text/html; charset=UTF-8'
        data = data.encode("utf-8")
    start_response(
        f"200 OK", [
            ("Content-type", content_type),
        ]
    )

    return iter([data])

serve(app)

