# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .t_me_url_type import TMeUrlType
from ..base_object import BaseObject


class TMeUrl(BaseObject):
    """
    Represents a URL linking to an internal Telegram entity
    
    Params:
        url (:class:`str`)
            URL
        
        type_ (:class:`TMeUrlType`)
            Type of the URL
        
    """

    ID: str = Field("tMeUrl", alias="@type")
    url: str
    type_: TMeUrlType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> TMeUrl:
        return TMeUrl.construct(**q)
