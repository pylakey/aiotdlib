# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetChatTitle(BaseObject):
    """
    Changes the chat title. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        title (:class:`str`)
            New title of the chat; 1-128 characters
        
    """

    ID: str = Field("setChatTitle", alias="@type")
    chat_id: int
    title: str = Field(..., min_length=1, max_length=128)

    @staticmethod
    def read(q: dict) -> SetChatTitle:
        return SetChatTitle.construct(**q)
