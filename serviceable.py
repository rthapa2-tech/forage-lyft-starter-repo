# implements serviceable interface
from abc import ABC,abstractmethod

class Serviceable:
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        raise NotImplemented