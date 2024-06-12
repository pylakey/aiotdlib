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
    BotCommandScope,
)


class GetCommands(BaseObject):
    """
    Returns the list of commands supported by the bot for the given user scope and language; for bots only

    :param language_code: A two-letter ISO 639-1 language code or an empty string
    :type language_code: :class:`String`
    :param scope: The scope to which the commands are relevant; pass null to get commands in the default bot command scope, defaults to None
    :type scope: :class:`BotCommandScope`, optional
    """

    ID: typing.Literal["getCommands"] = Field("getCommands", validation_alias="@type", alias="@type")
    language_code: String
    scope: typing.Optional[BotCommandScope] = None
