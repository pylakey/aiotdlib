# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import MessageSender
from ..base_object import BaseObject


class GetChatMember(BaseObject):
    """
    Returns information about a single member of a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param member_id: Member identifier
    :type member_id: :class:`MessageSender`
    
    """

    ID: str = Field("getChatMember", alias="@type")
    chat_id: int
    member_id: MessageSender

    @staticmethod
    def read(q: dict) -> GetChatMember:
        return GetChatMember.construct(**q)
