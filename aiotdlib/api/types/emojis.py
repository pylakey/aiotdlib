# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Emojis(BaseObject):
    """
    Represents a list of emoji
    
    Params:
        emojis (:obj:`list[str]`)
            List of emojis
        
    """

    ID: str = Field("emojis", alias="@type")
    emojis: list[str]

    @staticmethod
    def read(q: dict) -> Emojis:
        return Emojis.construct(**q)
