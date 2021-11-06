from dataclasses import dataclass
from plantwatering.codes import WaterCodes


@dataclass(frozen=True)
class WateringSummary:

    date: str
    time: str
    code: WaterCodes

    def __str__(self) -> str:
        return (
            f"Watering completed {self.date} at {self.time} with code: {self.code.name}"
        )
