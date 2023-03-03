from cars import Car

class Uber_X(Car):
    brand = str
    model = str

    def __init__(self, license, driver, brand, model):
        super().__init__(id, license, driver,)
        self.brand = brand
        self.model = model
        
        
