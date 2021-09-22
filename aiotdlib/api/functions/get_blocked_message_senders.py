# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetBlockedMessageSenders(BaseObject):
    """
    Returns users and chats that were blocked by the current user
    
    :param offset: Number of users and chats to skip in the result; must be non-negative
    :type offset: :class:`int`
    
    :param limit: The maximum number of users and chats to return; up to 100
    :type limit: :class:`int`
    
    """

    ID: str = Field("getBlockedMessageSenders", alias="@type")
    offset: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetBlockedMessageSenders:
        return GetBlockedMessageSenders.construct(**q)
