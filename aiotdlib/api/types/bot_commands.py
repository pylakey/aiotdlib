# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .bot_command import BotCommand
from ..base_object import BaseObject


class BotCommands(BaseObject):
    """
    Contains a list of bot commands
    
    :param bot_user_id: Bot's user identifier
    :type bot_user_id: :class:`int`
    
    :param commands: List of bot commands
    :type commands: :class:`list[BotCommand]`
    
    """

    ID: str = Field("botCommands", alias="@type")
    bot_user_id: int
    commands: list[BotCommand]

    @staticmethod
    def read(q: dict) -> BotCommands:
        return BotCommands.construct(**q)
