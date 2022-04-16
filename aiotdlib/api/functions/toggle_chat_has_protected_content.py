# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleChatHasProtectedContent(BaseObject):
    """
    Changes the ability of users to save, forward, or copy chat content. Supported only for basic groups, supergroups and channels. Requires owner privileges
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param has_protected_content: New value of has_protected_content
    :type has_protected_content: :class:`bool`
    
    """

    ID: str = Field("toggleChatHasProtectedContent", alias="@type")
    chat_id: int
    has_protected_content: bool

    @staticmethod
    def read(q: dict) -> ToggleChatHasProtectedContent:
        return ToggleChatHasProtectedContent.construct(**q)
