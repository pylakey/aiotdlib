# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import BotCommand
from ..types import BotCommandScope


class SetCommands(BaseObject):
    """
    Sets the list of commands supported by the bot for the given user scope and language; for bots only
    
    Params:
        scope (:class:`BotCommandScope`)
            The scope to which the commands are relevant
        
        language_code (:class:`str`)
            A two-letter ISO 639-1 country code. If empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands
        
        commands (:obj:`list[BotCommand]`)
            List of the bot's commands
        
    """

    ID: str = Field("setCommands", alias="@type")
    scope: BotCommandScope
    language_code: str
    commands: list[BotCommand]

    @staticmethod
    def read(q: dict) -> SetCommands:
        return SetCommands.construct(**q)
