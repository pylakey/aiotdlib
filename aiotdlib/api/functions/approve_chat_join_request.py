# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ApproveChatJoinRequest(BaseObject):
    """
    Approves pending join request in a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param user_id: Identifier of the user, which request will be approved
    :type user_id: :class:`int`
    
    """

    ID: str = Field("approveChatJoinRequest", alias="@type")
    chat_id: int
    user_id: int

    @staticmethod
    def read(q: dict) -> ApproveChatJoinRequest:
        return ApproveChatJoinRequest.construct(**q)
