import logging
from hbmqtt.client._client import MQTTClient
import asyncio

logger = logging.getLogger(__name__)

C = MQTTClient()

@asyncio.coroutine
def test_coro():
    yield from C.connect(uri='mqtt://iot.eclipse.org:1883/', username=None, password=None)
    ret = yield from C.subscribe([
                 {'filter': '$SYS/broker/uptime', 'qos': 0x01},
             ])
    logger.info("Subscribed")
    logger.info(repr(ret))
    yield from asyncio.sleep(10)
    yield from C.unsubscribe(['$SYS/broker/uptime'])
    logger.info("UnSubscribed")
    yield from C.disconnect()


if __name__ == '__main__':
    formatter = "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=formatter)
    asyncio.get_event_loop().run_until_complete(test_coro())