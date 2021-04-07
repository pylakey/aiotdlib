# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_member import ChatMember
from ..base_object import BaseObject


class ChatMembers(BaseObject):
    """
    Contains a list of chat members
    
    Params:
        total_count (:class:`int`)
            Approximate total count of chat members found
        
        members (:obj:`list[ChatMember]`)
            A list of chat members
        
    """

    ID: str = Field("chatMembers", alias="@type")
    total_count: int
    members: list[ChatMember]

    @staticmethod
    def read(q: dict) -> ChatMembers:
        return ChatMembers.construct(**q)
