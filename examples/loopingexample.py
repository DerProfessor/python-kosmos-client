import time
import logging

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
_LOGGER.addHandler(console)

from kosmos_client import KosmosClient, KosmosEvent, KosmosDevice, KosmosScope, KosmosLocation, \
    KosmosNotFoundError, KosmosError


def on_auth_ok(kosmos: KosmosClient):
    _LOGGER.info(f"auth okay  on {kosmos}...")


def on_device_created(kosmos: KosmosClient, device: KosmosDevice):
    _LOGGER.info(f"new device on {kosmos} {device}")


def on_device_attribute_changed(kosmos: KosmosClient, device: KosmosDevice, attribute: str, value):
    _LOGGER.info(f"change on {kosmos} {device} - set {attribute} to {value}")


if __name__ == '__main__':
    with KosmosClient("http://localhost:18080", "user", "pass",
                      subs={
                          KosmosEvent.auth_ok: on_auth_ok,
                          KosmosEvent.device_created: on_device_created,
                          KosmosEvent.device_attribute_updated: on_device_attribute_changed
                      }) as kosmos:
        _LOGGER.info(f"is connected:{kosmos.is_connected()}")
        try:
            kosmos.add_schema({
                "failures": [

                ],
                "$schema": "http://json-schema.org/draft-07/schema#",
                "examples": [

                ],
                "additionalProperties": False,
                "title": "TutorialOccupancy",
                "type": "object",
                "required": ["occupancy"],
                "properties": {
                    "occupancy": {
                        "description": "Defines whether the sensors detected motion",
                        "readOnly": False,
                        "title": "occupancy",
                        "type": "boolean"
                    }
                },
                "$id": "https://kosmos-lab.de/schema/TutorialOccupancy2.json"
            })

        except KosmosError as e:
            _LOGGER.info(e)
            pass

        try:
            kosmos.add_device("tutorial_occupancy_1", {"occupancy": False},
                              schema="https://kosmos-lab.de/schema/TutorialOccupancy2.json")
        except KosmosError as e:
            _LOGGER.info(e)
            pass

        while kosmos.is_connected():
            kosmos.set_attribute("tutorial_occupancy_1", "occupancy", True)
            time.sleep(60)
            kosmos.set_attribute("tutorial_occupancy_1", "occupancy", False)
            time.sleep(60)

        # kosmos.stop()
