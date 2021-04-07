# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatFilter


class EditChatFilter(BaseObject):
    """
    Edits existing chat filter. Returns information about the edited chat filter
    
    Params:
        chat_filter_id (:class:`int`)
            Chat filter identifier
        
        filter_ (:class:`ChatFilter`)
            The edited chat filter
        
    """

    ID: str = Field("editChatFilter", alias="@type")
    chat_filter_id: int
    filter_: ChatFilter = Field(..., alias='filter')

    @staticmethod
    def read(q: dict) -> EditChatFilter:
        return EditChatFilter.construct(**q)
