# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class BotCommand(BaseObject):
    """
    Represents a command supported by a bot
    
    :param command: Text of the bot command
    :type command: :class:`str`
    
    :param param_description: Description of the bot command
    :type param_description: :class:`str`
    
    """

    ID: str = Field("botCommand", alias="@type")
    command: str
    param_description: str

    @staticmethod
    def read(q: dict) -> BotCommand:
        return BotCommand.construct(**q)
