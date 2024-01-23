"""
# Документация для модуля render_template.py

## Описание
Модуль `render_template.py` предоставляет функционал для чтения HTML-шаблонов и возврата их в виде строки.

## Зависимости
- Python 3.x

## Функции

### render_template(template_name)
Функция для чтения HTML-шаблона из файла и возвращения его в виде строки.

#### Параметры
- `template_name` (строка): Имя файла HTML-шаблона.

#### Возвращаемые значения
- Содержимое HTML-шаблона в виде строки.
"""

def render_template(template_name):
    """
    Функция для чтения HTML-шаблона из файла и возвращения его в виде строки.
    
    :param template_name: Имя файла HTML-шаблона.
    :return: Содержимое HTML-шаблона в виде строки.
    """
    with open(template_name, 'r', encoding='utf-8') as f:
        html_str = f.read()
    return html_str
