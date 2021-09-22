# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChatStatisticsInviterInfo(BaseObject):
    """
    Contains statistics about number of new members invited by a user
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    :param added_member_count: Number of new members invited by the user
    :type added_member_count: :class:`int`
    
    """

    ID: str = Field("chatStatisticsInviterInfo", alias="@type")
    user_id: int
    added_member_count: int

    @staticmethod
    def read(q: dict) -> ChatStatisticsInviterInfo:
        return ChatStatisticsInviterInfo.construct(**q)
