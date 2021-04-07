# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetTextEntities(BaseObject):
    """
    Returns all entities (mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses) contained in the text. Can be called synchronously
    
    Params:
        text (:class:`str`)
            The text in which to look for entites
        
    """

    ID: str = Field("getTextEntities", alias="@type")
    text: str

    @staticmethod
    def read(q: dict) -> GetTextEntities:
        return GetTextEntities.construct(**q)
