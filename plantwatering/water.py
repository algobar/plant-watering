from plantwatering.codes import WaterCodes
from watering_system import WateringSystem

WATERING_TIME_SECONDS: float = 1.0
MAX_MOISTURE_THRESHOLD: float = 1.0  # normalized from 0 to 1


def water(system: WateringSystem, interval: float, moisture_threshold: float):
    """Runs the main sequence of executing the plant watering:

    - Checking pump status
    - Checking conditions that would not be ideal for watering
    - Watering for a predetermined interval

    Return status indicates if watering is successful, otherwise error
    """

    if system.is_tank_empty():
        return WaterCodes.EMPTY_TANK

    elif system.get_moisture_level() > moisture_threshold:
        return WaterCodes.THRESHOLD_EXCEEDED

    system.water(interval)

    return WaterCodes.SUCCESS