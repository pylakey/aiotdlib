# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .bot_command import BotCommand
from ..base_object import BaseObject


class BotInfo(BaseObject):
    """
    Provides information about a bot and its supported commands
    
    Params:
        param_description (:class:`str`)
            Long description shown on the user info page
        
        commands (:obj:`list[BotCommand]`)
            A list of commands supported by the bot
        
    """

    ID: str = Field("botInfo", alias="@type")
    param_description: str
    commands: list[BotCommand]

    @staticmethod
    def read(q: dict) -> BotInfo:
        return BotInfo.construct(**q)
