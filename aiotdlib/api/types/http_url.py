# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class HttpUrl(BaseObject):
    """
    Contains an HTTP URL
    
    Params:
        url (:class:`str`)
            The URL
        
    """

    ID: str = Field("httpUrl", alias="@type")
    url: str

    @staticmethod
    def read(q: dict) -> HttpUrl:
        return HttpUrl.construct(**q)
