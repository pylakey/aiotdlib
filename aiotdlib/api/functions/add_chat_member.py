# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AddChatMember(BaseObject):
    """
    Adds a new member to a chat. Members can't be added to private or secret chats

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param user_id: Identifier of the user
    :type user_id: :class:`Int53`
    :param forward_limit: The number of earlier messages from the chat to be forwarded to the new member; up to 100. Ignored for supergroups and channels, or if the added user is a bot
    :type forward_limit: :class:`Int32`
    """

    ID: typing.Literal["addChatMember"] = "addChatMember"
    chat_id: Int53
    user_id: Int53
    forward_limit: Int32
