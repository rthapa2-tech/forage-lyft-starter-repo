from car import Car
from engine import Engine
from sternman_engine import SternmanEngine
from battery import Battery
from spindler_battery import SpindlerBattery
import datetime

engine1 = SternmanEngine(False)
battery1 = SpindlerBattery(datetime.date(2023,9,7), datetime.date(2022,9,6))

car1 = Car(engine1,battery1)
print(car1.needs_service())