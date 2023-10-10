import base64
import os
import re

class Photos:
    def photos_json(self):
        data = {}
        directory = './static/db/images/'
        for filename in os.scandir(directory):
            if filename.is_file():
                image = open(filename.path, 'rb')
                image_read = image.read()
                image_64_encode = base64.b64encode(image_read)
                base_64 = image_64_encode.decode()
                data[filename.name] = base_64
        return data
    
class Blog:
    def posts_json(self):
        data = {}
        directory = './static/db/blog'
        pattern = '[\w-]+?(?=\.)'
        for filename in os.scandir(directory):
            if filename.is_file():
                idPost = re.search(pattern,filename.path)
                id = idPost.group()
                with open(filename.path) as f:
                    contents = f.readlines()
                    for content in contents:
                        post_array = content.split(":")
                        data[id] = {'title': post_array[0], 'subtitle': post_array[1], 'content': post_array[2]}
        return data
    

class Post:
    def post_json(self, idpost):
        data = {}
        directory = './static/db/blog'
        pattern = '[\w-]+?(?=\.)'
        for filename in os.scandir(directory):
            if filename.is_file():
                idPost = re.search(pattern,filename.path)
                id = idPost.group()
                if id == idpost:
                    with open(filename.path) as f:
                        contents = f.readlines()
                        for content in contents:
                            post_array = content.split(":")
                            data[id] = {'title': post_array[0], 'subtitle': post_array[1], 'content': post_array[2]}
                            return data
                else:
                    continue
        return data
        
