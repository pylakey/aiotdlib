# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteAllRevokedChatInviteLinks(BaseObject):
    """
    Deletes all revoked chat invite links created by a given chat administrator. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        creator_user_id (:class:`int`)
            User identifier of a chat administrator, which links will be deleted. Must be an identifier of the current user for non-owner
        
    """

    ID: str = Field("deleteAllRevokedChatInviteLinks", alias="@type")
    chat_id: int
    creator_user_id: int

    @staticmethod
    def read(q: dict) -> DeleteAllRevokedChatInviteLinks:
        return DeleteAllRevokedChatInviteLinks.construct(**q)
