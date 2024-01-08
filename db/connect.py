import pymysql
import json
import base64
import pymysql.cursors
from db.config_db import user, host, password, db_name

def get_products_from_db():
    json_product = []
    try:
        connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected")

        try: 
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM `products`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    json_product.append(row)
                for product in json_product:
                    image_data = product['image'].decode('utf-8')
                    product['image'] = image_data
                json_string = json.dumps(json_product)
                return json_string
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)

