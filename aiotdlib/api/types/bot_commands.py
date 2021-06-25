# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .bot_command import BotCommand
from ..base_object import BaseObject


class BotCommands(BaseObject):
    """
    Contains a list of bot commands
    
    Params:
        bot_user_id (:class:`int`)
            Bot's user identifier
        
        commands (:obj:`list[BotCommand]`)
            List of bot commands
        
    """

    ID: str = Field("botCommands", alias="@type")
    bot_user_id: int
    commands: list[BotCommand]

    @staticmethod
    def read(q: dict) -> BotCommands:
        return BotCommands.construct(**q)
