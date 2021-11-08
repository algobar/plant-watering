from plantwatering.codes import WaterCodes
from plantwatering.watering_factory import systems
from plantwatering.notification import BroadcastNotificationService, NotificationService
from plantwatering.summary import WateringSummary
from plantwatering.watering_system import WateringSystem
from plantwatering.water import water
from datetime import datetime, date


def run(
        system_name: str,
        messenger_name: str,
        interval: int,
        moisture_threshold=0,
        **kwargs
) -> None:

    watering_system: WateringSystem = systems.create(system_name, **kwargs)
    notification_service: NotificationService = BroadcastNotificationService()
    messenger = messaging.create(messenger_name, **kwargs)
    notification_service.add_messenger(messenger)

    return_code: WaterCodes = water(
        watering_system, interval, moisture_threshold=moisture_threshold
    )

    data = WateringSummary(
        date=str(date.today()),
        time=str(datetime.now().time()),
        code=return_code
    )

    notification_service.notify(data)
