from enum import Enum, auto


class WaterCodes(Enum):

    SUCCESS = auto()
    EMPTY_TANK = auto()
    THRESHOLD_EXCEEDED = auto()
