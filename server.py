from waitress import serve
from templates_view.home_view import HomeView
from templates_view.product_view import ProductView
from render_template import render_template
from serve_file import serve_static_file
from json_obj.get_json import GetProducts
import mimetypes

urls = {
    '/': HomeView,
    '/product/': ProductView,
    '/api/products': GetProducts,
}

def app(environ, start_response):
    path = environ.get("PATH_INFO")
    if path.startswith("/product/") and "/product/" in urls:
        view_class = urls["/product/"]
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
        data = render_template(template_name='templates/404.html', context={})
        data = data.encode("utf-8")

    mime_type, encoding = mimetypes.guess_type(path)
    content_type = mime_type if mime_type else 'text/html'
    if encoding:
        content_type += f'; charset={encoding}'
    start_response("200 OK", [("Content-type", content_type)])
    return iter([data])

if __name__ == "__main__":
    serve(app)
