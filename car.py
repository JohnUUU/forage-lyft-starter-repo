from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tires=None):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced() \
            or (self.tires != None and self.tires.tires_should_be_serviced())
