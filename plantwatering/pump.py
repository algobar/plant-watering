'''Module to hold pump definition, pump error codes

'''
from abc import ABC, abstractmethod


class Pump(ABC):

    @abstractmethod
    def turn_on(self):
        ...

    @abstractmethod
    def turn_off(self):
        ...

    @abstractmethod
    def is_tank_empty(self):
        ...

    @abstractmethod
    def get_soil_level(self):
        ...


class RelayPump(Pump):

    def turn_on(self):
        return super().turn_on()
    
    def turn_off(self):
        return super().turn_off()

    def is_tank_empty(self):
        return super().is_tank_empty()
    
    def get_soil_level(self):
        return super().get_soil_level()