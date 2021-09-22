# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatPermissions
from ..base_object import BaseObject


class SetChatPermissions(BaseObject):
    """
    Changes the chat members permissions. Supported only for basic groups and supergroups. Requires can_restrict_members administrator right
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param permissions: New non-administrator members permissions in the chat
    :type permissions: :class:`ChatPermissions`
    
    """

    ID: str = Field("setChatPermissions", alias="@type")
    chat_id: int
    permissions: ChatPermissions

    @staticmethod
    def read(q: dict) -> SetChatPermissions:
        return SetChatPermissions.construct(**q)
