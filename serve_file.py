import mimetypes

def serve_file(path, start_response):
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
    if path.startswith("/src/"):
        return serve_file(path, start_response)