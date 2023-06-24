# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class TransferChatOwnership(BaseObject):
    """
    Changes the owner of a chat. The current user must be a current owner of the chat. Use the method canTransferOwnership to check whether the ownership can be transferred from the current session. Available only for supergroups and channel chats

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param user_id: Identifier of the user to which transfer the ownership. The ownership can't be transferred to a bot or to a deleted user
    :type user_id: :class:`Int53`
    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    """

    ID: typing.Literal["transferChatOwnership"] = "transferChatOwnership"
    chat_id: Int53
    user_id: Int53
    password: String
