from car import Car
from engine import Engine
from capulet_engine import CapuletEngine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from battery import Battery
from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery
import datetime

class CarFactory:
    def __init__(self):
        pass

    def create_calliope(current_date,last_service_date,current_mileage,last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        calliope = Car(engine,battery)
        return calliope
    
    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        glissade =  Car(engine,battery)
        return glissade

    def create_palindrome(current_date,last_service_date,warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        palindrome =  Car(engine,battery)
        return palindrome

    def create_rorscach(current_date,last_service_date,current_mileage,last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        rorscach = Car(engine,battery)
        return rorscach
    
    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        thovex = Car(engine, battery)
        return thovex
    
