# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ClearRecentlyFoundChats(BaseObject):
    """
    Clears the list of recently found chats
    
    """

    ID: str = Field("clearRecentlyFoundChats", alias="@type")

    @staticmethod
    def read(q: dict) -> ClearRecentlyFoundChats:
        return ClearRecentlyFoundChats.construct(**q)
