import time
from abc import ABC, abstractmethod
from plantwatering.pumps.pump import Pump


class WateringSystem(ABC):
    def __init__(self, pump: Pump, **kwargs) -> None:
        self.pump = pump

    @abstractmethod
    def is_tank_empty(self) -> bool:
        """Checks if tank is empty"""
        ...

    @abstractmethod
    def get_moisture_level(self) -> float:
        """Gets current soil level"""
        ...

    @abstractmethod
    def water(self, interval: float) -> None:
        """Waters for set interval"""
        ...


class TestSystem(WateringSystem):
    def is_tank_empty(self) -> bool:
        return False

    def get_moisture_level(self) -> float:
        return 0.0

    def water(self, interval: float) -> None:

        self.pump.turn_on()
        print("watering for", interval, "seconds")
        self.pump.turn_off()


class RPiWateringSystem(WateringSystem):
    def is_tank_empty(self) -> bool:

        return False

    def get_moisture_level(self) -> float:

        return 0.0

    def water(self, interval: float) -> None:
        """Turns on pump for set amount of time"""

        self.pump.turn_on()
        time.sleep(interval)
        self.pump.turn_off()
