# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import BotCommandScope


class DeleteCommands(BaseObject):
    """
    Deletes commands supported by the bot for the given user scope and language; for bots only
    
    :param scope: The scope to which the commands are relevant
    :type scope: :class:`BotCommandScope`
    
    :param language_code: A two-letter ISO 639-1 country code or an empty string
    :type language_code: :class:`str`
    
    """

    ID: str = Field("deleteCommands", alias="@type")
    scope: BotCommandScope
    language_code: str

    @staticmethod
    def read(q: dict) -> DeleteCommands:
        return DeleteCommands.construct(**q)
