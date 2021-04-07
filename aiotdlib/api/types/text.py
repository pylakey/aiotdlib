# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Text(BaseObject):
    """
    Contains some text
    
    Params:
        text (:class:`str`)
            Text
        
    """

    ID: str = Field("text", alias="@type")
    text: str

    @staticmethod
    def read(q: dict) -> Text:
        return Text.construct(**q)
