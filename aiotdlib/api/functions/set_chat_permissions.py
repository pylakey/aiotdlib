# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatPermissions


class SetChatPermissions(BaseObject):
    """
    Changes the chat members permissions. Supported only for basic groups and supergroups. Requires can_restrict_members administrator right
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        permissions (:class:`ChatPermissions`)
            New non-administrator members permissions in the chat
        
    """

    ID: str = Field("setChatPermissions", alias="@type")
    chat_id: int
    permissions: ChatPermissions

    @staticmethod
    def read(q: dict) -> SetChatPermissions:
        return SetChatPermissions.construct(**q)
