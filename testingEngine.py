from engine import Engine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from capulet_engine import CapuletEngine


def engine_needs_service(engine):
    if engine.needs_service() == True:
        print("yes")
    else:
        print("no")


engine1 = WilloughbyEngine(100000, 45000)
engine2 = SternmanEngine(True)
engine3 = CapuletEngine(100000, 45000)

engine_needs_service(engine1)
print("Expected: no")
engine_needs_service(engine2)
print("Expected: yes")
engine_needs_service(engine3)
print("Expected: yes")
