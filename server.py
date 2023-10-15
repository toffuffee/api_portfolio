from waitress import serve
import json

def render_template(template_name, context={}):
    html_str=""
    with open(template_name, 'r') as f:
        html_str=f.read()
        html_str=html_str.format(**context)
    return html_str

# Формирование JSON объекта
def json_get():
    data = {
        "1": 1,
        "2": 2,
    }
    json_data = json.dumps(data)
    result = bytes(json_data, 'utf-8')
    return [result]


def home(environ):
    return render_template('templates/index.html', context={})

def contact_us(environ):
    return render_template('templates/contact.html', context={})

def contact2(environ):
    return render_template('templates/2.html', context={})

def app(environ, start_response):
    path= environ.get("PATH_INFO")
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
        page = home(environ)
    elif path == "/contact":
        page = contact_us(environ)
    elif path == "/contact/2":
        page = contact2(environ)

    # Пример получение JSON
    elif path == "/api/test":
        page = json_get()
        start_response(
            f"200 OK", [
            ("Content-type", "application/json"),
            ]
        )
        return page
    

    else:
        page = render_template('templates/404.html', context={"path":path})
    page = page.encode("utf-8")

    start_response(
        f"200 OK", [
            ("Content-type", "text/html"),
        ]
    )
    return iter([page])

serve(app)