# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteRevokedChatInviteLink(BaseObject):
    """
    Deletes revoked chat invite links. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        invite_link (:class:`str`)
            Invite link to revoke
        
    """

    ID: str = Field("deleteRevokedChatInviteLink", alias="@type")
    chat_id: int
    invite_link: str

    @staticmethod
    def read(q: dict) -> DeleteRevokedChatInviteLink:
        return DeleteRevokedChatInviteLink.construct(**q)
