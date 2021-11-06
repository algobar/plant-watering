import time
from abc import ABC, abstractmethod
from pumps import Pump


class WateringSystem(ABC):
    @abstractmethod
    def is_tank_empty(self) -> bool:
        """Checks if tank is empty"""
        ...

    @abstractmethod
    def get_moisture_level(self) -> float:
        """Gets current soil level"""
        ...

    @abstractmethod
    def water(interval: float) -> None:
        """Waters for set interval"""
        ...


class RPiWateringSystem(WateringSystem):
    def __init__(self, pump: Pump) -> None:

        self.pump = pump

    def is_tank_empty(self) -> bool:

        return False

    def get_moisture_level(self) -> float:

        return 0.0

    def water(self, interval: float) -> None:
        """Turns on pump for set amount of time"""

        self.pump.turn_on()
        time.sleep(interval)
        self.pump.turn_off()
