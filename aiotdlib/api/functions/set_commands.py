# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import BotCommand
from ..types import BotCommandScope
from ..base_object import BaseObject


class SetCommands(BaseObject):
    """
    Sets the list of commands supported by the bot for the given user scope and language; for bots only
    
    :param scope: The scope to which the commands are relevant
    :type scope: :class:`BotCommandScope`
    
    :param language_code: A two-letter ISO 639-1 country code. If empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands
    :type language_code: :class:`str`
    
    :param commands: List of the bot's commands
    :type commands: :class:`list[BotCommand]`
    
    """

    ID: str = Field("setCommands", alias="@type")
    scope: BotCommandScope
    language_code: str
    commands: list[BotCommand]

    @staticmethod
    def read(q: dict) -> SetCommands:
        return SetCommands.construct(**q)
