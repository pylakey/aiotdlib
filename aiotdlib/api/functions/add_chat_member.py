# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class AddChatMember(BaseObject):
    """
    Adds a new member to a chat. Members can't be added to private or secret chats
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param user_id: Identifier of the user
    :type user_id: :class:`int`
    
    :param forward_limit: The number of earlier messages from the chat to be forwarded to the new member; up to 100. Ignored for supergroups and channels
    :type forward_limit: :class:`int`
    
    """

    ID: str = Field("addChatMember", alias="@type")
    chat_id: int
    user_id: int
    forward_limit: int

    @staticmethod
    def read(q: dict) -> AddChatMember:
        return AddChatMember.construct(**q)
