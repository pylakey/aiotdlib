# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetSuitableDiscussionChats(BaseObject):
    """
    Returns a list of basic group and supergroup chats, which can be used as a discussion group for a channel. Returned basic group chats must be first upgraded to supergroups before they can be set as a discussion group. To set a returned supergroup as a discussion group, access to its old messages must be enabled using toggleSupergroupIsAllHistoryAvailable first
    
    """

    ID: str = Field("getSuitableDiscussionChats", alias="@type")

    @staticmethod
    def read(q: dict) -> GetSuitableDiscussionChats:
        return GetSuitableDiscussionChats.construct(**q)
