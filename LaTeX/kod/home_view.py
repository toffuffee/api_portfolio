"""
# Документация для модуля home_view.py

## Описание
Модуль `home_view.py` содержит класс `HomeView`, который представляет собой представление для отображения главной страницы.

## Зависимости
- Python 3.x
- templates_view.base_view
- render_template

## Классы

### HomeView(View)
Класс представления для страницы главной страницы.

#### Атрибуты
- `template` (строка): Путь к HTML-шаблону главной страницы.

#### Методы

##### `get(environ)`
Метод для обработки GET-запроса и отображения главной страницы.

###### Параметры
- `environ` (словарь): Словарь окружения WSGI.

###### Возвращаемые значения
- Возвращает HTML-страницу главной страницы в виде строки.
"""

from templates_view.base_view import View
from render_template import render_template

class HomeView(View):
    """
    Класс представления для страницы главной страницы.
    """
    template = 'templates/index.html'

    def get(self, environ):
        """
        Метод для обработки GET-запроса и отображения главной страницы.
        
        :param environ: Словарь окружения WSGI.
        :return: HTML-страница главной страницы в виде строки.
        """
        return render_template(template_name=self.template)
