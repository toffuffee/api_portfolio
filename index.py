from waitress import serve
from api import Photos, Blog, Post
import requests

photos = Photos()
posts = Blog()
post = Post()

def render_template(template_name='../api_portfolio/templates/index.html', context={}):
    html_str=""
    with open(template_name, 'r') as f:
        html_str=f.read()
        html_str=html_str.format(**context)
    return html_str

def app(environ, start_response):
    path= environ.get("PATH_INFO")
    if path == "/":
        data = index(environ)
    elif path == "/blog":
        data = blog(environ)
    elif path == "/images":
        data = images(environ)
    elif path == "/api/photos":
        return photos.photos_json() 
    elif path == "/api/blog":
        return posts.posts_json() 
    else:
        data = render_template(template_name='../api_portfolio/templates/404.html', context={"path":path})
    data = data.encode("utf-8")
    start_response(
        f"200 OK", [
            ("Content-type", "text/html"),
            ("Content-Lenght", str(len("abc")))
        ]
    )
    return iter([data])


# API
# @app.route('/api/photos')
def api_photos():
    return photos.photos_json()

# @app.route('/api/blog')
def api_blog():
    return posts.posts_json()

# @app.route('/api/blog/<postid>/')
def api_blog_post(postid):
    return post.post_json(postid)

# @app.route('/test', methods=['POST', 'GET'])
# def test():
#     return render_template('test.html')

# @app.route('/test/add', methods=['POST', 'GET'])
# def testAdd():
#     if request.method == 'POST':
#         title = request.form['title']
#         subtitle = request.form['subtitle']
#         content = request.form['content']

#         add_post = open(f"./static/blog/{title}.txt","w+")
#         add_post.write(f"{title}:{subtitle}:{content}")
#         add_post.close()
#         print(title, subtitle, content)
#     return redirect(f'/blog/{title}')

# Redirect

# @app.route('/images')
def images(environ):
    return render_template(template_name='../api_portfolio/templates/images.html', context={})

# @app.route('/blog')
def blog(environ):
    return render_template(template_name='../api_portfolio/templates/blog.html', context={})

# @app.route('/blog/<postid>/')
def blogpost(postid):
    return render_template(template_name='../api_portfolio/templates/postpage.html', context={})

# @app.route('/')
def index(environ):
    return render_template(template_name='../api_portfolio/templates/index.html', context={})



# if __name__ == '__main__':
#     app.run(debug=True)

serve(app)