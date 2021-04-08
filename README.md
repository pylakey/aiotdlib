# aiotdlib

## Python asyncio wrapper for [TDLib](https://github.com/tdlib/td). 
> All types and functions are generated automatically based on [TD tl-schema](https://github.com/tdlib/td/blob/master/td/generate/scheme/td_api.tl) 

> Tested with TDLib v1.7.3 only. Support for other versions of TDLib is not guaranteed

> Prebuilt binary (v1.7.3) **only for macOS** included.
> You can use your own binary by passing `library_path` argument to `Client` class constructor

> You need to get your **api_id** and **api_hash** first.
> Read more in [Telegram docs](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id)

### Basic example

```python
import asyncio
import logging

from aiotdlib import Client

API_ID = 12345
API_HASH = "00112233445566778899aabbccddeeff"
PHONE_NUMBER = ""


async def main():
    client = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        phone_number=PHONE_NUMBER
    )

    async with client:
        me = await client.api.get_me()
        logging.info(f"Successfully logged in as {me.json()}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

### Registering event handler

```python
import asyncio
import logging

from aiotdlib import Client
from aiotdlib.api import API, BaseObject, UpdateNewMessage

API_ID = 12345
API_HASH = "00112233445566778899aabbccddeeff"
PHONE_NUMBER = ""


async def on_update_new_message(client: Client, update: UpdateNewMessage):
    chat_id = update.message.chat_id

    # api field of client instance contains all TDLib functions, for example get_chat
    chat = await client.api.get_chat(chat_id)
    logging.info(f'Message received in chat {chat.title}')


async def any_event_handler(client: Client, update: BaseObject):
    logging.info(f'Event of type {update.ID} received')


async def main():
    client = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        phone_number=PHONE_NUMBER
    )

    # Registering event handler for 'updateNewMessage' event
    # You can register many handlers for certain event type
    client.add_event_handler(on_update_new_message, update_type=API.Types.UPDATE_NEW_MESSAGE)
    
    # You can register handler for special event type "*". 
    # It will be called for each received event
    client.add_event_handler(any_event_handler, update_type=API.Types.ANY)

    async with client:
        # idle() will run client until it's stopped
        await client.idle()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

### Middlewares

```python

import asyncio
import logging

from aiotdlib import Client, HandlerCallable
from aiotdlib.api import API, BaseObject, UpdateNewMessage

API_ID = 12345
API_HASH = "00112233445566778899aabbccddeeff"
PHONE_NUMBER = ""


async def some_pre_updates_work(event: BaseObject):
    logging.info(f"Before call all update handlers for event {event.ID}")


async def some_post_updates_work(event: BaseObject):
    logging.info(f"After call all update handlers for event {event.ID}")


# Middlewares are useful for opening database connections for example
# Note that call_next argument would always be passed as keyword argument,
# so it should be called "call_next" only.
async def my_middleware(client: Client, event: BaseObject, *, call_next: HandlerCallable):
    await some_pre_updates_work(event)

    try:
        await call_next(client, event)
    finally:
        await some_post_updates_work(event)


async def on_update_new_message(client: Client, update: UpdateNewMessage):
    logging.info('on_update_new_message handler called')


async def main():
    client = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        phone_number=PHONE_NUMBER
    )

    client.add_event_handler(on_update_new_message, update_type=API.Types.UPDATE_NEW_MESSAGE)

    # Registering middleware.
    # Note that middleware would be called for EVERY EVENT.
    # Don't use them for long-running tasks as it could be heavy performance hit
    # You can add as much middlewares as you want. 
    # They would be called in order you've added them
    client.add_middleware(my_middleware)

    async with client:
        await client.idle()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```