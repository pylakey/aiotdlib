# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatInviteLinks(BaseObject):
    """
    Returns invite links for a chat created by specified administrator. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param creator_user_id: User identifier of a chat administrator. Must be an identifier of the current user for non-owner
    :type creator_user_id: :class:`Int53`
    :param offset_date: Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning
    :type offset_date: :class:`Int32`
    :param offset_invite_link: Invite link starting after which to return invite links; use empty string to get results from the beginning
    :type offset_invite_link: :class:`String`
    :param limit: The maximum number of invite links to return; up to 100
    :type limit: :class:`Int32`
    :param is_revoked: Pass true if revoked links needs to be returned instead of active or expired
    :type is_revoked: :class:`Bool`
    """

    ID: typing.Literal["getChatInviteLinks"] = "getChatInviteLinks"
    chat_id: Int53
    creator_user_id: Int53
    offset_date: Int32
    offset_invite_link: String
    limit: Int32
    is_revoked: Bool = False
