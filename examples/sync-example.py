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
    print(f'login ok {await kosmos.login()}')
    schema = await kosmos.get_schema("https://kosmos-lab.de/schema/Heater.json")
    print(schema)


if __name__ ==  '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())