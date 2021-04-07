# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import BotCommand


class SetCommands(BaseObject):
    """
    Sets the list of commands supported by the bot; for bots only
    
    Params:
        commands (:obj:`list[BotCommand]`)
            List of the bot's commands
        
    """

    ID: str = Field("setCommands", alias="@type")
    commands: list[BotCommand]

    @staticmethod
    def read(q: dict) -> SetCommands:
        return SetCommands.construct(**q)
