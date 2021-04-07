# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RemoveChatActionBar(BaseObject):
    """
    Removes a chat action bar without any other action
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("removeChatActionBar", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> RemoveChatActionBar:
        return RemoveChatActionBar.construct(**q)
