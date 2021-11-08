from abc import ABC, abstractmethod
from typing import List, Protocol
from .summary import WateringSummary
from dataclasses import dataclass, field


class MessengerProtocol(Protocol):
    """Defines the standard interface for a messenger"""

    def notify(message: WateringSummary) -> None:
        ...


class NotificationService(ABC):
    """Abstract notification service that notifies a messenger"""

    @abstractmethod
    def add_messenger(self, messenger: MessengerProtocol) -> None:
        ...

    @abstractmethod
    def notify(self, message: WateringSummary) -> None:
        ...


@dataclass
class BroadcastNotificationService(NotificationService):
    """Maintains multiple messengers for notifications"""

    _messengers: List = field(default_factory=list)

    def add_messenger(self, messenger: MessengerProtocol) -> None:
        """Appends a new messenger to the list the service maintains"""
        self._messengers.append(messenger)

    def notify(self, message: WateringSummary) -> None:
        """Passes the message to each of the messengers"""

        for messenger in self._messengers:
            messenger.notify(message)
