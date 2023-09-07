'''from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
'''

class Car:
    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery
    
    def needs_service(self):
        if Engine.needs_service() or Battery.needs_service():
            return True
        else:
            return False