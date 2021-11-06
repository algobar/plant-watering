from typing import Protocol


class Relay(Protocol):
    """Defines the interface for a relay"""

    def turn_on(self) -> None:
        ...

    def turn_off(self) -> None:
        ...


OutputDevice = OutputDevice(pin=pin, active_high=True, initial_value=False)
