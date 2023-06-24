# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteAllRevokedChatInviteLinks(BaseObject):
    """
    Deletes all revoked chat invite links created by a given chat administrator. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param creator_user_id: User identifier of a chat administrator, which links will be deleted. Must be an identifier of the current user for non-owner
    :type creator_user_id: :class:`Int53`
    """

    ID: typing.Literal["deleteAllRevokedChatInviteLinks"] = "deleteAllRevokedChatInviteLinks"
    chat_id: Int53
    creator_user_id: Int53
