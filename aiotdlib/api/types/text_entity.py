# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .text_entity_type import TextEntityType
from ..base_object import BaseObject


class TextEntity(BaseObject):
    """
    Represents a part of the text that needs to be formatted in some unusual way
    
    :param offset: Offset of the entity, in UTF-16 code units
    :type offset: :class:`int`
    
    :param length: Length of the entity, in UTF-16 code units
    :type length: :class:`int`
    
    :param type_: Type of the entity
    :type type_: :class:`TextEntityType`
    
    """

    ID: str = Field("textEntity", alias="@type")
    offset: int
    length: int
    type_: TextEntityType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> TextEntity:
        return TextEntity.construct(**q)
