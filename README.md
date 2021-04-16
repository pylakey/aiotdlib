# aiotdlib - Python asyncio Telegram client based on [TDLib](https://github.com/tdlib/td)

[![PyPI version shields.io](https://img.shields.io/pypi/v/aiotdlib.svg)](https://pypi.python.org/pypi/aiotdlib/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/aiotdlib.svg)](https://pypi.python.org/pypi/aiotdlib/)
[![PyPI license](https://img.shields.io/pypi/l/aiotdlib.svg)](https://pypi.python.org/pypi/aiotdlib/)

## Features

* All types and functions are generated automatically
  from [tl schema](https://github.com/tdlib/td/blob/master/td/generate/scheme/td_api.tl)
* All types and functions come with validation and good IDE type hinting (thanks
  to [Pydantic](https://github.com/samuelcolvin/pydantic))
* A set of high-level API methods which makes work with tdlib much simpler

> Tested with TDLib v1.7.3 only. Support for other versions of TDLib is not guaranteed

> Prebuilt binary (v1.7.3) **only for macOS** included.
> You can use your own binary by passing `library_path` argument to `Client` class constructor

## Requirements

* Python 3.9+
* Get your **api_id** and **api_hash**. Read more
  in [Telegram docs](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id)

## Installation

```shell
pip install aiotdlib
```

## Example

```python
import asyncio
import logging

from aiotdlib import Client

API_ID = 5172829
API_HASH = "7ae1bef25a2194cf31d6321fd228cac2"
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

### Events handlers

```python
import asyncio
import logging

from aiotdlib import Client
from aiotdlib.api import API, BaseObject, UpdateNewMessage

API_ID = 5172829
API_HASH = "7ae1bef25a2194cf31d6321fd228cac2"
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

### Bot command handler

```python
import asyncio
import logging

from aiotdlib import Client
from aiotdlib.api import UpdateNewMessage

API_ID = 5172829
API_HASH = "7ae1bef25a2194cf31d6321fd228cac2"
PHONE_NUMBER = ""

client = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    phone_number=PHONE_NUMBER
)


async def on_start_command(client: Client, update: UpdateNewMessage):
    await client.send_text(update.message.chat_id, "Have a good day! :)")


# Note: bot_command_handler method is universal and can be used directly or as decorator
# Registering handler for '/help' command
@client.bot_command_handler(command='help')
async def on_help_command(client: Client, update: UpdateNewMessage):
    await client.send_text(update.message.chat_id, "I will help you!")


async def main():
    # Note: bot_command_handler method is universal and can be used directly or as decorator
    # Registering handler for '/start' command
    client.bot_command_handler(on_start_command, command='start')

    async with client:
        await client.idle()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

### Proxy

```python

import asyncio
import logging

from aiotdlib import Client, ClientProxySettings, ClientProxyType

API_ID = 5172829
API_HASH = "7ae1bef25a2194cf31d6321fd228cac2"
PHONE_NUMBER = ""


async def main():
  client = Client(
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

  async with client:
    await client.idle()


if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  asyncio.run(main())
```

## LICENSE

This project is licensed under the terms of the [MIT](https://github.com/pylakey/aiotdlib/blob/master/LICENSE) license.