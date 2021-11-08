"""Module to hold pump definition, pump error codes"""

from abc import ABC, abstractmethod


class Pump(ABC):
    """Abstract class representing a controllable pump"""

    @abstractmethod
    def turn_on(self) -> None:
        """Turns on the pump"""
        ...

    @abstractmethod
    def turn_off(self) -> None:
        """Turns off the pump"""
        ...


class TestPump(Pump):
    def turn_on(self) -> None:
        print("pump is on!")

    def turn_off(self) -> None:
        print("pump is off!")
