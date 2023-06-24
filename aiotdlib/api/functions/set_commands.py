# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    BotCommand,
    BotCommandScope,
)


class SetCommands(BaseObject):
    """
    Sets the list of commands supported by the bot for the given user scope and language; for bots only

    :param language_code: A two-letter ISO 639-1 language code. If empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands
    :type language_code: :class:`String`
    :param commands: List of the bot's commands
    :type commands: :class:`Vector[BotCommand]`
    :param scope: The scope to which the commands are relevant; pass null to change commands in the default bot command scope, defaults to None
    :type scope: :class:`BotCommandScope`, optional
    """

    ID: typing.Literal["setCommands"] = "setCommands"
    language_code: String
    commands: Vector[BotCommand]
    scope: typing.Optional[BotCommandScope] = None
