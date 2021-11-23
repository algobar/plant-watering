from .summary import WateringSummary
from abc import ABC, abstractmethod
import yagmail


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


class EmailMessenger:
    """Email based messaging"""

    def __init__(self, sender: str, recipient: str) -> None:

        self._sender = sender
        self._recipient = recipient

    def notify(self, message: WateringSummary) -> None:
        """emails the message to the provided email"""

        yagmail.SMTP(self._sender).send(
            self._recipient, "water summary", str(message)
        )
