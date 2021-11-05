# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatJoinRequest(BaseObject):
    """
    Describes a user that sent a join request and waits for administrator approval
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    :param date: Point in time (Unix timestamp) when the user sent the join request
    :type date: :class:`int`
    
    :param bio: A short bio of the user
    :type bio: :class:`str`
    
    """

    ID: str = Field("chatJoinRequest", alias="@type")
    user_id: int
    date: int
    bio: str

    @staticmethod
    def read(q: dict) -> ChatJoinRequest:
        return ChatJoinRequest.construct(**q)
