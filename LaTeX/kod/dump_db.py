"""
# Документация для модуля dump_database.py

## Описание
Модуль `dump_database.py` предоставляет функционал для создания дампа базы данных MySQL с использованием утилиты mysqldump.

## Зависимости
- Python 3.x
- getpass
- subprocess
- datetime

## Функции

### dump_database(host, port, username, password, database, output_file)
Функция для создания дампа базы данных MySQL.

#### Параметры
- `host` (строка): Адрес хоста базы данных.
- `port` (строка): Порт базы данных.
- `username` (строка): Имя пользователя базы данных.
- `password` (строка): Пароль пользователя базы данных.
- `database` (строка): Имя базы данных.
- `output_file` (строка): Путь к файлу, в который будет сохранен дамп.

#### Возвращаемые значения
- Выводит сообщение об успешном создании дампа или сообщение об ошибке в случае неудачи.

### main()
Основная функция для выполнения дампа базы данных при запуске скрипта.

#### Параметры
- (None)

#### Возвращаемые значения
- (None)
"""

import getpass
import subprocess
import datetime

def dump_database(host, port, username, password, database, output_file):
    """
    Функция для создания дампа базы данных MySQL.
    
    :param host: Адрес хоста базы данных.
    :param port: Порт базы данных.
    :param username: Имя пользователя базы данных.
    :param password: Пароль пользователя базы данных.
    :param database: Имя базы данных.
    :param output_file: Путь к файлу, в который будет сохранен дамп.
    :return: Выводит сообщение об успешном создании дампа или сообщение об ошибке в случае неудачи.
    """
    password_input = getpass.getpass(prompt=f"Введите пароль для пользователя {username}: ")

    dump_command = [
        r'C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe',
        '--host', host,
        '--port', str(port),
        '--user', username,
        f'--password={password_input}',
        '--result-file', output_file,
        database,
    ]

    process = subprocess.Popen(dump_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Ошибка при выполнении дампа базы данных:\n{stderr.decode('utf-8')}")
    else:
        print(f"Дамп базы данных успешно создан в файле: {output_file}")

if __name__ == "__main__":
    db_host = 'localhost'
    db_port = '3306'
    db_username = 'root'
    db_name = 'shop'

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    dump_filename = f"database_dump_{timestamp}.sql"

    dump_database(db_host, db_port, db_username, None, db_name, dump_filename)
