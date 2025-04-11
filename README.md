# aiotdlib - Python asyncio Telegram client based on [TDLib](https://github.com/tdlib/td)

[![PyPI version shields.io](https://img.shields.io/pypi/v/aiotdlib.svg)](https://pypi.python.org/pypi/aiotdlib/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/aiotdlib.svg)](https://pypi.python.org/pypi/aiotdlib/)
[![PyPI license](https://img.shields.io/pypi/l/aiotdlib.svg)](https://pypi.python.org/pypi/aiotdlib/)

> [!WARNING]
> This library is still in development, so any updates before version 1.0.0 may include breaking changes. Please be cautious and pin the library version when using it. If you wish to update, I recommend reviewing the Git commit history.

> This wrapper is actual
> for **[TDLib v1.8.46](https://github.com/tdlib/td/commit/b498497bbfd6b80c86f800b3546a0170206317d3)**
>
> This package includes prebuilt TDLib binaries for macOS (arm64) and Debian (amd64).
> You can use your own binary by passing `library_path` argument to `Client` class constructor. Make sure it's built
> from [this commit](https://github.com/tdlib/td/commit/b498497bbfd6b80c86f800b3546a0170206317d3). Compatibility with
> other versions of library is not guaranteed.

## Features

* All types and functions are generated automatically
  from [tl schema](https://github.com/tdlib/td/blob/8f19c751dc296cedb9a921badb7a02a8c0cb1aeb/td/generate/scheme/td_api.tl)
* All types and functions come with validation and good IDE type hinting (thanks
  to [Pydantic](https://github.com/samuelcolvin/pydantic))
* A set of high-level API methods which makes work with tdlib much simpler

## Requirements

* Python 3.9+
* Get your **api_id** and **api_hash**. Read more
  in [Telegram docs](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id)

## Installation

### PyPI

```shell
pip install aiotdlib
```

or if you use [Poetry](https://python-poetry.org)

```shell
poetry add aiotdlib
```

## Examples

### Base example

```python
import asyncio
import logging

from aiotdlib import Client, ClientSettings

API_ID = 123456
API_HASH = ""
PHONE_NUMBER = ""


async def main():
    client = Client(
        settings=ClientSettings(
            api_id=API_ID,
            api_hash=API_HASH,
            phone_number=PHONE_NUMBER
        )
    )

    async with client:
        me = await client.api.get_me()
        logging.info(f"Successfully logged in as {me.model_dump_json()}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

Any parameter of Client class could be also set via environment variables with prefix `AIOTDLIB_*`.

```python
import asyncio
import logging

from aiotdlib import Client


async def main():
    async with Client() as client:
        me = await client.api.get_me()
        logging.info(f"Successfully logged in as {me.model_dump_json()}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

and run it like this:

```shell
export AIOTDLIB_API_ID=123456
export AIOTDLIB_API_HASH=<my_api_hash>
export AIOTDLIB_BOT_TOKEN=<my_bot_token>
python main.py
```

### Events handlers

```python
import asyncio
import logging

from aiotdlib import Client, ClientSettings
from aiotdlib.api import API, BaseObject, UpdateNewMessage

API_ID = 123456
API_HASH = ""
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
        settings=ClientSettings(
            api_id=API_ID,
            api_hash=API_HASH,
            phone_number=PHONE_NUMBER
        )
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

### Bot command handler

```python
import logging

from aiotdlib import Client, ClientSettings
from aiotdlib.api import UpdateNewMessage

API_ID = 123456
API_HASH = ""
BOT_TOKEN = ""

bot = Client(
    settings=ClientSettings(
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
    )
)

# Note: bot_command_handler method is universal and can be used directly or as decorator
# Registering handler for '/help' command
@bot.bot_command_handler(command='help')
async def on_help_command(client: Client, update: UpdateNewMessage):
    # Each command handler registered with this method will update update.EXTRA field
    # with command related data: {'bot_command': 'help', 'bot_command_args': []}
    await client.send_text(update.message.chat_id, "I will help you!")


async def on_start_command(client: Client, update: UpdateNewMessage):
    # So this will print "{'bot_command': 'help', 'bot_command_args': []}"
    print(update.EXTRA)
    await client.send_text(update.message.chat_id, "Have a good day! :)")


async def on_custom_command(client: Client, update: UpdateNewMessage):
    # So when you send a message "/custom 1 2 3 test" 
    # So this will print "{'bot_command': 'custom', 'bot_command_args': ['1', '2', '3', 'test']}"
    print(update.EXTRA)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # Registering handler for '/start' command
    bot.bot_command_handler(on_start_command, command='start')
    bot.bot_command_handler(on_custom_command, command='custom')
    bot.run()
```

### Proxy

```python

import asyncio
import logging

from aiotdlib import Client
from aiotdlib import ClientSettings
from aiotdlib import ClientProxySettings
from aiotdlib import ClientProxyType

API_ID = 123456
API_HASH = ""
PHONE_NUMBER = ""


async def main():
    client = Client(
        settings=ClientSettings(
            api_id=API_ID,
            api_hash=API_HASH,
            phone_number=PHONE_NUMBER,
            proxy_settings=ClientProxySettings(
                host="10.0.0.1",
                port=3333,
                type=ClientProxyType.SOCKS5,
                username="aiotdlib",
                password="somepassword",
            )
        )
    )

    async with client:
        await client.idle()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

### Middlewares

```python

import asyncio
import logging

from aiotdlib import Client, HandlerCallable, ClientSettings
from aiotdlib.api import API, BaseObject, UpdateNewMessage

API_ID = 12345
API_HASH = ""
PHONE_NUMBER = ""


async def some_pre_updates_work(event: BaseObject):
    logging.info(f"Before call all update handlers for event {event.ID}")


async def some_post_updates_work(event: BaseObject):
    logging.info(f"After call all update handlers for event {event.ID}")


# Note that call_next argument would always be passed as keyword argument,
# so it should be called "call_next" only.
async def my_middleware(client: Client, event: BaseObject, /, *, call_next: HandlerCallable):
    # Middlewares useful for opening database connections for example
    await some_pre_updates_work(event)

    try:
        await call_next(client, event)
    finally:
        await some_post_updates_work(event)


async def on_update_new_message(client: Client, update: UpdateNewMessage):
    logging.info('on_update_new_message handler called')


async def main():
    client = Client(
        settings=ClientSettings(
            api_id=API_ID,
            api_hash=API_HASH,
            phone_number=PHONE_NUMBER
        )
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

## LICENSE

This project is licensed under the terms of the [MIT](https://github.com/pylakey/aiotdlib/blob/master/LICENSE) license.
