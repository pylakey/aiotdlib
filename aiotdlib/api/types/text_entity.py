# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .text_entity_type import TextEntityType
from ..base_object import BaseObject


class TextEntity(BaseObject):
    """
    Represents a part of the text that needs to be formatted in some unusual way
    
    Params:
        offset (:class:`int`)
            Offset of the entity, in UTF-16 code units
        
        length (:class:`int`)
            Length of the entity, in UTF-16 code units
        
        type_ (:class:`TextEntityType`)
            Type of the entity
        
    """

    ID: str = Field("textEntity", alias="@type")
    offset: int
    length: int
    type_: TextEntityType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> TextEntity:
        return TextEntity.construct(**q)
