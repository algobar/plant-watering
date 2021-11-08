from .summary import WateringSummary
from abc import ABC, abstractmethod


class Messenger(ABC):
    def __init__(self, **kwargs) -> None:
        ...

    @abstractmethod
    def notify(message: WateringSummary) -> None:
        ...


class PrintingMessenger:
    """Service that prints messages to console"""

    def notify(self, message: WateringSummary) -> None:
        """prints the message to the console"""
        print(str(message))
