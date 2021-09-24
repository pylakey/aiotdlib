# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatFilter


class GetChatFilterDefaultIconName(BaseObject):
    """
    Returns default icon name for a filter. Can be called synchronously
    
    :param filter_: Chat filter
    :type filter_: :class:`ChatFilter`
    
    """

    ID: str = Field("getChatFilterDefaultIconName", alias="@type")
    filter_: ChatFilter = Field(..., alias='filter')

    @staticmethod
    def read(q: dict) -> GetChatFilterDefaultIconName:
        return GetChatFilterDefaultIconName.construct(**q)
