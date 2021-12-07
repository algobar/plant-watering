from .summary import WateringSummary
from abc import ABC, abstractmethod
import yagmail
import os


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

        pwd = os.environ.get(self._sender, None)

        yagmail.SMTP(user=self._sender, password=pwd).send(
            self._recipient, "water summary", str(message)
        )
