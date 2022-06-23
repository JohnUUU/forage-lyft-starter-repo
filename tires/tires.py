from abc import ABC, abstractmethod, abstractproperty


class Tires(ABC):
    @abstractmethod
    def tires_should_be_serviced(self):
        pass
