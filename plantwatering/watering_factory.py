from gpiozero import OutputDevice
from plantwatering.pumps.pump import TestPump
from plantwatering.watering_system import (
    RPiWateringSystem,
    TestSystem,
    WateringSystem,
)
from plantwatering.pumps.relay_pump import RelayPump


def build_rpi_watering_system(pin: int, **kwargs) -> WateringSystem:
    """Creates a raspberry pi watering system controlled by a relay pump

    Args:
        pin (int): which pin to run the raspberry pi relay on

    Returns:
        WateringSystem: [description]
    """

    relay: OutputDevice = OutputDevice(
        pin=pin, active_high=True, initial_value=False
    )

    pump: RelayPump = RelayPump(relay)

    return RPiWateringSystem(pump)


def build_test_system(**kwargs):

    pump: TestPump = TestPump()

    return TestSystem(pump)


class WateringFactory:
    def __init__(self) -> None:
        self._systems: dict = {}

    def register(self, name: str, builder):

        if name in self._systems:
            raise KeyError(f"{name} already exists!")

        self._systems[name] = builder

    def create(self, name, **kwargs):

        return self._systems[name](**kwargs)


systems = WateringFactory()
systems.register("raspberry_pi", build_rpi_watering_system)
systems.register("test", build_test_system)
