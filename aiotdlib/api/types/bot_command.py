# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class BotCommand(BaseObject):
    """
    Represents a command supported by a bot
    
    Params:
        command (:class:`str`)
            Text of the bot command
        
        param_description (:class:`str`)
            Description of the bot command
        
    """

    ID: str = Field("botCommand", alias="@type")
    command: str
    param_description: str

    @staticmethod
    def read(q: dict) -> BotCommand:
        return BotCommand.construct(**q)
