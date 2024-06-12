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
    ChatMemberStatus,
    MessageSender,
)


class SetChatMemberStatus(BaseObject):
    """
    Changes the status of a chat member; requires can_invite_users member right to add a chat member, can_promote_members administrator right to change administrator rights of the member, and can_restrict_members administrator right to change restrictions of a user. This function is currently not suitable for transferring chat ownership; use transferChatOwnership instead. Use addChatMember or banChatMember if some additional parameters needs to be passed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param member_id: Member identifier. Chats can be only banned and unbanned in supergroups and channels
    :type member_id: :class:`MessageSender`
    :param status: The new status of the member in the chat
    :type status: :class:`ChatMemberStatus`
    """

    ID: typing.Literal["setChatMemberStatus"] = Field("setChatMemberStatus", validation_alias="@type", alias="@type")
    chat_id: Int53
    member_id: MessageSender
    status: ChatMemberStatus
