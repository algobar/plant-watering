from dataclasses import dataclass, field
from .notification import MessengerProtocol

from .messenger import PrintingMessenger, EmailMessenger


@dataclass
class MessengerFactory:

    _messengers: dict = field(default_factory=dict)

    def register(self, name: str, messenger: MessengerProtocol):

        if name in self._messengers:
            raise KeyError(f"{name} already registered")
        self._messengers[name] = messenger

    def create(self, name: str, **kwargs):

        return self._messengers[name](**kwargs)


messaging = MessengerFactory()
messaging.register(PrintingMessenger.__name__, PrintingMessenger)
messaging.register(EmailMessenger.__name__, EmailMessenger)
