from plantwatering.pumps import Pump
from plantwatering.relay import Relay


class RelayPump(Pump):
    """Pump controlled via a electrical relay"""

    def __init__(self, relay: Relay):

        self._relay: Relay = relay

    def turn_on(self) -> None:
        """Access the relay and turns on the pump"""
        self._relay.on()

    def turn_off(self) -> None:
        """Access the relay and turns off the pump"""
        self._relay.off()
