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


class DeleteCommands(BaseObject):
    """
    Deletes commands supported by the bot for the given user scope and language; for bots only

    :param language_code: A two-letter ISO 639-1 language code or an empty string
    :type language_code: :class:`String`
    :param scope: The scope to which the commands are relevant; pass null to delete commands in the default bot command scope, defaults to None
    :type scope: :class:`BotCommandScope`, optional
    """

    ID: typing.Literal["deleteCommands"] = "deleteCommands"
    language_code: String
    scope: typing.Optional[BotCommandScope] = None
