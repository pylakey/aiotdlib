# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class EditChatInviteLink(BaseObject):
    """
    Edits a non-primary invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param invite_link: Invite link to be edited
    :type invite_link: :class:`String`
    :param name: Invite link name; 0-32 characters
    :type name: :class:`String`
    :param expiration_date: Point in time (Unix timestamp) when the link will expire; pass 0 if never
    :type expiration_date: :class:`Int32`
    :param member_limit: The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited
    :type member_limit: :class:`Int32`
    :param creates_join_request: Pass true if users joining the chat via the link need to be approved by chat administrators. In this case, member_limit must be 0
    :type creates_join_request: :class:`Bool`
    """

    ID: typing.Literal["editChatInviteLink"] = "editChatInviteLink"
    chat_id: Int53
    invite_link: String
    name: String = Field("", max_length=32)
    expiration_date: Int32 = 0
    member_limit: Int32 = 0
    creates_join_request: Bool = False
