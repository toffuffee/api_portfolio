"""
# Документация для модуля image_view.py

## Описание
Модуль `image_view.py` содержит класс `ImageView`, который представляет собой представление для отображения страницы с изображением.

## Зависимости
- Python 3.x
- templates_view.base_view
- render_template

## Классы

### ImageView(View)
Класс представления для страницы с изображением.

#### Атрибуты
- `template` (строка): Путь к HTML-шаблону страницы с изображением.

#### Методы

##### `get(environ)`
Метод для обработки GET-запроса и отображения страницы с изображением.

###### Параметры
- `environ` (словарь): Словарь окружения WSGI.

###### Возвращаемые значения
- Возвращает HTML-страницу с изображением в виде строки.
"""

from templates_view.base_view import View
from render_template import render_template

class ImageView(View):
    """
    Класс представления для страницы с изображением.
    """
    template = 'templates/image_page.html'

    def get(self, environ):
        """
        Метод для обработки GET-запроса и отображения страницы с изображением.
        
        :param environ: Словарь окружения WSGI.
        :return: HTML-страница с изображением в виде строки.
        """
        return render_template(template_name=self.template)
