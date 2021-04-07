# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AddChatMember(BaseObject):
    """
    Adds a new member to a chat. Members can't be added to private or secret chats
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        user_id (:class:`int`)
            Identifier of the user
        
        forward_limit (:class:`int`)
            The number of earlier messages from the chat to be forwarded to the new member; up to 100. Ignored for supergroups and channels
        
    """

    ID: str = Field("addChatMember", alias="@type")
    chat_id: int
    user_id: int
    forward_limit: int

    @staticmethod
    def read(q: dict) -> AddChatMember:
        return AddChatMember.construct(**q)
