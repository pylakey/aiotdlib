# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .background_type import BackgroundType
from .document import Document
from ..base_object import BaseObject


class Background(BaseObject):
    """
    Describes a chat background
    
    :param id: Unique background identifier
    :type id: :class:`int`
    
    :param is_default: True, if this is one of default backgrounds
    :type is_default: :class:`bool`
    
    :param is_dark: True, if the background is dark and is recommended to be used with dark theme
    :type is_dark: :class:`bool`
    
    :param name: Unique background name
    :type name: :class:`str`
    
    :param document: Document with the background; may be null. Null only for filled backgrounds, defaults to None
    :type document: :class:`Document`, optional
    
    :param type_: Type of the background
    :type type_: :class:`BackgroundType`
    
    """

    ID: str = Field("background", alias="@type")
    id: int
    is_default: bool
    is_dark: bool
    name: str
    document: typing.Optional[Document] = None
    type_: BackgroundType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> Background:
        return Background.construct(**q)
