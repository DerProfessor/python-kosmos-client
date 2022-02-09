import logging

from kosmos_client import KosmosClient

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
_LOGGER.addHandler(console)
import asyncio


async def main():
    kosmos = KosmosClient("http://localhost:18080", "user", "pass")
    print(f'login ok {kosmos.login()}')
    schema = kosmos.get_schema("https://kosmos-lab.de/schema/DimmableLamp.json")
    print(schema)
    # print(await kosmos.list_devices())
    print(kosmos.get_device('virt_dim_lamp_0'))
    (kosmos.set_attribute('virt_dim_lamp_0', 'on', True))
    print(kosmos.get_device('virt_dim_lamp_0'))
    (kosmos.set_attribute('virt_dim_lamp_0', 'on', False))
    print(kosmos.get_device('virt_dim_lamp_0'))
    (await kosmos.set_attribute_async('virt_dim_lamp_0', 'on', True))
    print(await kosmos.get_device_async('virt_dim_lamp_0'))
    (await kosmos.set_attribute_async('virt_dim_lamp_0', 'on', False))
    print(await kosmos.get_device_async('virt_dim_lamp_0'))



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
