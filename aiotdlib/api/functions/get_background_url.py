# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import BackgroundType


class GetBackgroundUrl(BaseObject):
    """
    Constructs a persistent HTTP URL for a background
    
    Params:
        name (:class:`str`)
            Background name
        
        type_ (:class:`BackgroundType`)
            Background type
        
    """

    ID: str = Field("getBackgroundUrl", alias="@type")
    name: str
    type_: BackgroundType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> GetBackgroundUrl:
        return GetBackgroundUrl.construct(**q)
