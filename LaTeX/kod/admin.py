"""
# Документация для модуля admin_view.py

## Описание
Модуль `admin_view.py` содержит класс `AdminView`, который представляет собой представление для отображения админ-панели.

## Зависимости
- Python 3.x
- templates_view.base_view
- render_template

## Классы

### AdminView(View)
Класс представления для страницы админ-панели.

#### Атрибуты
- `template` (строка): Путь к HTML-шаблону страницы админ-панели.

#### Методы

##### `get(environ)`
Метод для обработки GET-запроса и отображения страницы админ-панели.

###### Параметры
- `environ` (словарь): Словарь окружения WSGI.

###### Возвращаемые значения
- Возвращает HTML-страницу админ-панели в виде строки.
"""

from templates_view.base_view import View
from render_template import render_template

class AdminView(View):
    """
    Класс представления для страницы админ-панели.
    """
    template = 'templates/admin.html'

    def get(self, environ):
        """
        Метод для обработки GET-запроса и отображения страницы админ-панели.
        
        :param environ: Словарь окружения WSGI.
        :return: HTML-страница админ-панели в виде строки.
        """
        return render_template(template_name=self.template)
