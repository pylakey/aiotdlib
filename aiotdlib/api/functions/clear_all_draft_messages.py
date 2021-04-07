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
    Clears draft messages in all chats
    
    Params:
        exclude_secret_chats (:class:`bool`)
            If true, local draft messages in secret chats will not be cleared
        
    """

    ID: str = Field("clearAllDraftMessages", alias="@type")
    exclude_secret_chats: bool

    @staticmethod
    def read(q: dict) -> ClearAllDraftMessages:
        return ClearAllDraftMessages.construct(**q)
