# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ClearAllDraftMessages(BaseObject):
    """
    Clears message drafts in all chats
    
    :param exclude_secret_chats: Pass true to keep local message drafts in secret chats
    :type exclude_secret_chats: :class:`bool`
    
    """

    ID: str = Field("clearAllDraftMessages", alias="@type")
    exclude_secret_chats: bool

    @staticmethod
    def read(q: dict) -> ClearAllDraftMessages:
        return ClearAllDraftMessages.construct(**q)
