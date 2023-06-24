# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    MessageSender,
)


class GetChatMember(BaseObject):
    """
    Returns information about a single member of a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param member_id: Member identifier
    :type member_id: :class:`MessageSender`
    """

    ID: typing.Literal["getChatMember"] = "getChatMember"
    chat_id: Int53
    member_id: MessageSender
