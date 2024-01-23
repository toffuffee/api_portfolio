"""
# Документация для модуля admin_login_view.py

## Описание
Модуль `admin_login_view.py` содержит класс `AdminLogin`, который представляет собой представление для отображения страницы входа в админ-панель.

## Зависимости
- Python 3.x
- templates_view.base_view
- render_template

## Классы

### AdminLogin(View)
Класс представления для страницы входа в админ-панель.

#### Атрибуты
- `template` (строка): Путь к HTML-шаблону страницы входа в админ-панель.

#### Методы

##### `get(environ)`
Метод для обработки GET-запроса и отображения страницы входа в админ-панель.

###### Параметры
- `environ` (словарь): Словарь окружения WSGI.

###### Возвращаемые значения
- Возвращает HTML-страницу входа в админ-панель в виде строки.
"""

from templates_view.base_view import View
from render_template import render_template

class AdminLogin(View):
    """
    Класс представления для страницы входа в админ-панель.
    """
    template = 'templates/admin_login.html'

    def get(self, environ):
        """
        Метод для обработки GET-запроса и отображения страницы входа в админ-панель.
        
        :param environ: Словарь окружения WSGI.
        :return: HTML-страница входа в админ-панель в виде строки.
        """
        return render_template(template_name=self.template)
