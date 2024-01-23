"""
# Документация для модуля connect.py

## Описание
Модуль `connect.py` содержит функции для работы с базой данных MySQL, включая получение изображений, информации об администраторе и вставку изображений.

## Зависимости
- Python 3.x
- pymysql
- json
- base64
- pymysql.cursors
- db_info.config_db

## Функции

### get_images_from_db()
Функция для получения изображений из базы данных.

#### Возвращаемые значения
- Возвращает JSON-строку, содержащую информацию об изображениях из базы данных.

### get_admin_info_from_db()
Функция для получения информации об администраторе из базы данных.

#### Возвращаемые значения
- Возвращает JSON-строку, содержащую информацию об администраторе из базы данных.

### insert_image_to_db(image_data, image_name=None, image_desc=None, image_country=None)
Функция для вставки изображения в базу данных.

#### Параметры
- `image_data` (байтовый объект): Данные изображения в виде байтов.
- `image_name` (строка, по умолчанию None): Название изображения.
- `image_desc` (строка, по умолчанию None): Описание изображения.
- `image_country` (строка, по умолчанию None): Страна, к которой относится изображение.

#### Возвращаемые значения
- (None)
"""

import pymysql
import json
import base64
import pymysql.cursors
from db_info.config_db import user, host, password, db_name

def get_images_from_db():
    """
    Функция для получения изображений из базы данных.
    
    :return: JSON-строка, содержащая информацию об изображениях из базы данных.
    """
    json_images = []
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
                select_all_rows = "SELECT * FROM `images`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    json_images.append(row)
                for product in json_images:
                    image_data = product['image'].decode('utf-8')
                    product['image'] = image_data
                json_string = json.dumps(json_images)
                return json_string
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)


def get_admin_info_from_db():
    """
    Функция для получения информации об администраторе из базы данных.
    
    :return: JSON-строка, содержащая информацию об администраторе из базы данных.
    """
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
                select_all_rows = "SELECT * FROM `admin`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    json_admin = row
                json_string = json.dumps(json_admin)
                return json_string
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)

def insert_image_to_db(image_data, image_name=None, image_desc=None, image_country=None):
    """
    Функция для вставки изображения в базу данных.
    
    :param image_data: Данные изображения в виде байтов.
    :param image_name: Название изображения.
    :param image_desc: Описание изображения.
    :param image_country: Страна, к которой относится изображение.
    :return: (None)
    """
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
                # Encode binary data as base64
                image_data_base64 = base64.b64encode(image_data).decode('utf-8')

                # Prepend the data URI prefix
                image_data_with_prefix = f"data:image/jpeg;base64,{image_data_base64}"

                insert_image_query = "INSERT INTO `images` (`image`, `image_name`, `image_desc`, `image_country`) VALUES (%s, %s, %s, %s)"
                cursor.execute(insert_image_query, (image_data_with_prefix, image_name, image_desc, image_country))
                connection.commit()
                print("Image successfully inserted into the database. ID:", cursor.lastrowid)
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)
