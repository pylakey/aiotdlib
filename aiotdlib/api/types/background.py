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
    
    Params:
        id (:class:`int`)
            Unique background identifier
        
        is_default (:class:`bool`)
            True, if this is one of default backgrounds
        
        is_dark (:class:`bool`)
            True, if the background is dark and is recommended to be used with dark theme
        
        name (:class:`str`)
            Unique background name
        
        document (:class:`Document`)
            Document with the background; may be null. Null only for filled backgrounds
        
        type_ (:class:`BackgroundType`)
            Type of the background
        
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
