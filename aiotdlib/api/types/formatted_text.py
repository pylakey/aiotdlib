# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .text_entity import TextEntity
from ..base_object import BaseObject


class FormattedText(BaseObject):
    """
    A text with some entities
    
    Params:
        text (:class:`str`)
            The text
        
        entities (:obj:`list[TextEntity]`)
            Entities contained in the text. Entities can be nested, but must not mutually intersect with each other. Pre, Code and PreCode entities can't contain other entities. Bold, Italic, Underline and Strikethrough entities can contain and to be contained in all other entities. All other entities can't contain each other
        
    """

    ID: str = Field("formattedText", alias="@type")
    text: str
    entities: list[TextEntity]

    @staticmethod
    def read(q: dict) -> FormattedText:
        return FormattedText.construct(**q)
