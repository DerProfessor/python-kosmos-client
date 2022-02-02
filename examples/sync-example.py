
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
                "additionalProperties": True,
                "title": "NoSchema",
                "type": "object",
                "properties": {
                },
                "$id": "https://kosmos-lab.de/schema/TestNoSchema.json"
            })

        except KosmosError as e:
            _LOGGER.warn(e)
            pass
        try:
            _LOGGER.info(kosmos.get_schema("https://kosmos-lab.de/schema/TestNoSchema.json"))
        except KosmosNotFoundError as e:
            _LOGGER.warn(e)
            pass
        try:
            _LOGGER.info(kosmos.list_schemas())
        except KosmosError as e:
            _LOGGER.warn(e)
            pass
        #kosmos.stop()
