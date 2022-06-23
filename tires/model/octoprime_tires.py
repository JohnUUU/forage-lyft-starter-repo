from abc import ABC
from tires.tires import Tires


class OctoprimeTires(Tires, ABC):
    def __init__(self, sensor_data):
        self.tire_wear = sensor_data

    def tires_should_be_serviced(self):
        return sum(self.tire_wear) >= 3
