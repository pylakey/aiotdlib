# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ProcessChatJoinRequest(BaseObject):
    """
    Handles a pending join request in a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param user_id: Identifier of the user that sent the request
    :type user_id: :class:`int`
    
    :param approve: Pass true to approve the request; pass false to decline it
    :type approve: :class:`bool`
    
    """

    ID: str = Field("processChatJoinRequest", alias="@type")
    chat_id: int
    user_id: int
    approve: bool

    @staticmethod
    def read(q: dict) -> ProcessChatJoinRequest:
        return ProcessChatJoinRequest.construct(**q)
