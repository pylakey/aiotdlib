# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class DeleteAllRevokedChatInviteLinks(BaseObject):
    """
    Deletes all revoked chat invite links created by a given chat administrator. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param creator_user_id: User identifier of a chat administrator, which links will be deleted. Must be an identifier of the current user for non-owner
    :type creator_user_id: :class:`int`
    
    """

    ID: str = Field("deleteAllRevokedChatInviteLinks", alias="@type")
    chat_id: int
    creator_user_id: int

    @staticmethod
    def read(q: dict) -> DeleteAllRevokedChatInviteLinks:
        return DeleteAllRevokedChatInviteLinks.construct(**q)
