from car.carclass import CarClass


class ElectroCare(CarClass):
    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battery = 100

    def description_battary(self):
        print(f"Этот автомобиль имеет мощность {self.battery}%")
