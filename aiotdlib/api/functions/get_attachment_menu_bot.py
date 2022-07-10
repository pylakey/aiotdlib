# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetAttachmentMenuBot(BaseObject):
    """
    Returns information about a bot that can be added to attachment menu
    
    :param bot_user_id: Bot's user identifier
    :type bot_user_id: :class:`int`
    
    """

    ID: str = Field("getAttachmentMenuBot", alias="@type")
    bot_user_id: int

    @staticmethod
    def read(q: dict) -> GetAttachmentMenuBot:
        return GetAttachmentMenuBot.construct(**q)
