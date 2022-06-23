from abc import ABC
from tires.tires import Tires


class CarriganTires(Tires, ABC):
    def __init__(self, sensor_data):
        self.tire_wear = sensor_data

    def tires_should_be_serviced(self):
        return any([tire >= 0.9 for tire in self.tire_wear])
