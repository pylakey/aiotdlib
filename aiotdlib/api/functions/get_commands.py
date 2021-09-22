# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import BotCommandScope
from ..base_object import BaseObject


class GetCommands(BaseObject):
    """
    Returns the list of commands supported by the bot for the given user scope and language; for bots only
    
    :param scope: The scope to which the commands are relevant
    :type scope: :class:`BotCommandScope`
    
    :param language_code: A two-letter ISO 639-1 country code or an empty string
    :type language_code: :class:`str`
    
    """

    ID: str = Field("getCommands", alias="@type")
    scope: BotCommandScope
    language_code: str

    @staticmethod
    def read(q: dict) -> GetCommands:
        return GetCommands.construct(**q)
