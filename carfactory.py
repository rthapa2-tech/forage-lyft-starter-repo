from car import Car
from engine import Engine
from capulet_engine import CapuletEngine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from battery import Battery
from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery
from tires import Tires
from carrigan_tires import CarriganTires
from octoprime_tires import OctoprimeTires
import datetime

class CarFactory:
    def __init__(self):
        pass

    def create_calliope(current_date,last_service_date,current_mileage,last_service_mileage, wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tires = OctoprimeTires(wear_array)
        calliope = Car(engine,battery,tires)
        return calliope
    
    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileage, wear_array):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tires = OctoprimeTires(wear_array)
        glissade =  Car(engine,battery,tires)
        return glissade

    def create_palindrome(current_date,last_service_date,warning_light_on, wear_array):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(wear_array)
        palindrome =  Car(engine,battery, tires)
        return palindrome

    def create_rorscach(current_date,last_service_date,current_mileage,last_service_mileage,wear_array):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tires = CarriganTires(wear_array)
        rorscach = Car(engine,battery)
        return rorscach
    
    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage, wear_array):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tires = CarriganTires(wear_array)
        thovex = Car(engine, battery, tires)
        return thovex
    
#car1 = CarFactory.create_palindrome(datetime.date(2023,9,7), datetime.date(2022,9,6),False,[0.8,0.8,0.8,0.8])
#print(car1.needs_service())