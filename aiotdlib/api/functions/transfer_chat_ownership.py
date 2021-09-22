# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class TransferChatOwnership(BaseObject):
    """
    Changes the owner of a chat. The current user must be a current owner of the chat. Use the method canTransferOwnership to check whether the ownership can be transferred from the current session. Available only for supergroups and channel chats
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param user_id: Identifier of the user to which transfer the ownership. The ownership can't be transferred to a bot or to a deleted user
    :type user_id: :class:`int`
    
    :param password: The password of the current user
    :type password: :class:`str`
    
    """

    ID: str = Field("transferChatOwnership", alias="@type")
    chat_id: int
    user_id: int
    password: str

    @staticmethod
    def read(q: dict) -> TransferChatOwnership:
        return TransferChatOwnership.construct(**q)
