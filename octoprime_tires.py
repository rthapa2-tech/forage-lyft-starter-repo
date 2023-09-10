from tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, wearArray):
        super().__init__()
        self.wearArray = wearArray

    def needs_service(self):
        sum = 0
        for wear in self.wearArray:
            sum += wear
        if sum >= 3:
            return True
        else:
            return False

