from abc import ABC, abstractmethod
from render_template import render_template

class View(ABC):
    template = ''
    

    @abstractmethod
    def get(self, environ):
        pass
    
