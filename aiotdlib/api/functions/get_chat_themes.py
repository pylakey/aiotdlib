# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatThemes(BaseObject):
    """
    Returns the list of available chat themes
    
    """

    ID: str = Field("getChatThemes", alias="@type")

    @staticmethod
    def read(q: dict) -> GetChatThemes:
        return GetChatThemes.construct(**q)
