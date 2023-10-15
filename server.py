from waitress import serve
from api import Blog, Post
import json

blogPage = Blog()

def render_template(template_name, context={}):
    html_str=""
    with open(template_name, 'r') as f:
        html_str=f.read()
        html_str=html_str.format(**context)
    return html_str
 
def pageDisplay(environ, path, context={}):
    return render_template(path, context)

def app(environ, start_response):
    path= environ.get("PATH_INFO")
    err = "404 Not found"
    test = "test"
    pages = {
        '/test': pageDisplay(environ, 'templates/test.html', context={'test': test}),
        '/': pageDisplay(environ, 'templates/index.html', context={}),
        '/blog': pageDisplay(environ, 'templates/blog.html', context={}),
    }
    # Подключение JS и CSS
    if path.startswith("/src/css/"):
        new_path = path.replace('/','',1)
        try:
            with open(new_path, 'rb') as f:
                content = f.read()
            start_response("200 OK", [("Content-type", "text/css")])
            return [content]
        except FileNotFoundError:
            start_response("404 Not Found", [("Content-type", "text/plain")])
            return [b"404 Not Found css/js"]
    if path.startswith("/src/js/"):
        new_path = path.replace('/','',1)
        try:
            with open(new_path, 'rb') as f:
                content = f.read()
            start_response("200 OK", [("Content-type", "text/javascript")])
            return [content]
        except FileNotFoundError:
            start_response("404 Not Found", [("Content-type", "text/plain")])
            return [b"404 Not Found css/js"]
        
    if path == "/":
        page = pages[path]
    elif path == "/blog":
        page = pages[path]
    elif path == "/test":
        page = pages[path]
    # Пример получение JSON
    elif path == "/api/blog":
        page = blogPage.posts_json()
        start_response(
            f"200 OK", [
            ("Content-type", "application/json"),
            ]
        )
        return page
    else:
        page = render_template('templates/404.html', context={"err":err})
    page = page.encode("utf-8")

    start_response(
        f"200 OK", [
            ("Content-type", "text/html"),
        ]
    )
    return iter([page])

serve(app)