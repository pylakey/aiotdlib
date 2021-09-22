# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .text_entity import TextEntity
from ..base_object import BaseObject


class TextEntities(BaseObject):
    """
    Contains a list of text entities
    
    :param entities: List of text entities
    :type entities: :class:`list[TextEntity]`
    
    """

    ID: str = Field("textEntities", alias="@type")
    entities: list[TextEntity]

    @staticmethod
    def read(q: dict) -> TextEntities:
        return TextEntities.construct(**q)
