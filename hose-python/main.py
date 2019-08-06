import asyncio
import time
import signal
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

def run(loop):
    nc = NATS()

    options = {
        "servers": ["nats://username:password@nats-01.cryptoquote.io:4222"],
        "io_loop": loop,
    }

    yield from nc.connect(**options)

    @asyncio.coroutine
    def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))

    # "*" matches any token, at any level of the subject.
    # list to all markets on binance
    yield from nc.subscribe("hose.*.binance.>", cb=message_handler)

    # full hose
    # yield from nc.subscribe("hose.>", cb=message_handler)

    # listen to BTCUSD system wide
    yield from nc.subscribe("hose.*.*.btcusd", cb=message_handler)

    # listen to all Trades
    # yield from nc.subscribe("hose.trades.>", cb=message_handler)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    try:
        loop.run_forever()
    finally:
        loop.close()
