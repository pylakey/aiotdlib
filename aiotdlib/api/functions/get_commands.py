# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import BotCommandScope


class GetCommands(BaseObject):
    """
    Returns the list of commands supported by the bot for the given user scope and language; for bots only
    
    Params:
        scope (:class:`BotCommandScope`)
            The scope to which the commands are relevant
        
        language_code (:class:`str`)
            A two-letter ISO 639-1 country code or an empty string
        
    """

    ID: str = Field("getCommands", alias="@type")
    scope: BotCommandScope
    language_code: str

    @staticmethod
    def read(q: dict) -> GetCommands:
        return GetCommands.construct(**q)
