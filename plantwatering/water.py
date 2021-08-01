from src.pump import RelayPump, PumpStatus
import time
import argparse

WATERING_TIME_SECONDS: float = 1.0
MAX_MOISTURE_THRESHOLD: float= 1.0  # normalized from 0 to 1


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", type=float, default=WATERING_TIME_SECONDS)
    parser.add_argument("--threshold", type=float, default=MAX_MOISTURE_THRESHOLD)
    
    return parser.parse_args()

def water(pump: "Pump", interval: float, moisture_threshold: float):
    '''Runs the main sequence of executing the plant watering, which involves the following:

        - Checking pump status
        - Checking conditions that would not be ideal for watering
        - "Turning on" the pump, i.e, starting the relay
        - Waiting a predetermined amount of time
        - Turning off the pump

        Return status indicates if watering is successful, otherwise a specific error is returned
    '''

    if pump.is_tank_empty():
        return ""

    elif pump.get_soil_level() > moisture_threshold:
        return ""

    pump.turn_on()

    time.sleep(interval)

    pump.turn_off()

    return ""

if __name__ == "__main__":

    args = parse_args()
    pump = RelayPump()
    
    water(
            pump=pump,
            interval=args.interval,
            moisture_threshold=args.threshold
        )
