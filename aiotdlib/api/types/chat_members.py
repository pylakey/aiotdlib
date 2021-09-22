# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_member import ChatMember
from ..base_object import BaseObject


class ChatMembers(BaseObject):
    """
    Contains a list of chat members
    
    :param total_count: Approximate total count of chat members found
    :type total_count: :class:`int`
    
    :param members: A list of chat members
    :type members: :class:`list[ChatMember]`
    
    """

    ID: str = Field("chatMembers", alias="@type")
    total_count: int
    members: list[ChatMember]

    @staticmethod
    def read(q: dict) -> ChatMembers:
        return ChatMembers.construct(**q)
