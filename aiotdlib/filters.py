from collections import Callable, Coroutine
from typing import Any

from aiotdlib.api import BaseObject, MessageText, UpdateNewMessage

FilterCallable = Callable[[BaseObject], Coroutine[Any, Any, bool]]


# Some predefined filters
async def text_message_filter(update: BaseObject):
    return isinstance(update, UpdateNewMessage) and isinstance(update.message.content, MessageText)


def create_bot_command_filter(command: str = None):
    async def bot_command_filter(update: BaseObject) -> bool:
        if not isinstance(update, UpdateNewMessage) or not isinstance(update.message.content, MessageText):
            return False

        message_text = update.message.content.text.text

        if not message_text.startswith('/'):
            return False

        [bot_command, *bot_command_args] = message_text.lstrip('/').split()

        update.EXTRA['bot_command'] = bot_command
        update.EXTRA['bot_command_args'] = bot_command_args

        return not bool(command) or command == bot_command

    return bot_command_filter
