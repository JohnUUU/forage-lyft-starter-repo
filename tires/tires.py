from abc import ABC, abstractmethod, abstractproperty


class Tires(ABC):
    tire_wear = abstractproperty()

    @abstractmethod
    def tires_should_be_serviced(self):
        pass
