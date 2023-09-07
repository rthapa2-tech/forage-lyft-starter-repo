from battery import Battery
from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery
import datetime

def battery_needs_service(battery):
    if battery.needs_service() == True:
        print("yes")
    else:
        print("no")

battery1 = SpindlerBattery(datetime.date(2023,9,7), datetime.date(2020,9,6))
battery2 = NubbinBattery(datetime.date(2023,9,7), datetime.date(2020,9,6))

battery_needs_service(battery1)
battery_needs_service(battery2)