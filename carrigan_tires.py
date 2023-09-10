from tires import Tires

class CarriganTires(Tires):
    def __init__(self, wearArray):
        super().__init__()
        self.wearArray = wearArray
    
    def needs_service(self):
        needsService = False
        for wear in self.wearArray:
            if wear >=0.9:
                needsService = True    
        return needsService