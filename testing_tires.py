from tires import Tires
from carrigan_tires import CarriganTires
from octoprime_tires import OctoprimeTires

def tires_need_service(Tires):
    if Tires.needs_service():
        print("yes")
    else:
        print("no")

tire1 = CarriganTires([0.8,0.1,0.1,0.9])
tire2 = OctoprimeTires([0.8,0.1,0.1,0.9])

tires_need_service(tire1)
print("Expected: yes")
tires_need_service(tire2)
print("Expected: no")