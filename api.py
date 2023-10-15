import base64
import os
import re
import json
    
class Blog:
    def posts_json(self):
        data = {}
        directory = './src/db/blog'
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
        json_data = json.dumps(data)
        result = bytes(json_data, 'utf-8')
        return [result]
    
class Post:
    def post_json(self, idpost):
        data = {}
        directory = './src/db/blog'
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
        json_data = json.dumps(data)
        result = bytes(json_data, 'utf-8')
        return [result]