# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetRecentlyOpenedChats(BaseObject):
    """
    Returns recently opened chats, this is an offline request. Returns chats in the order of last opening
    
    :param limit: The maximum number of chats to be returned
    :type limit: :class:`int`
    
    """

    ID: str = Field("getRecentlyOpenedChats", alias="@type")
    limit: int

    @staticmethod
    def read(q: dict) -> GetRecentlyOpenedChats:
        return GetRecentlyOpenedChats.construct(**q)
