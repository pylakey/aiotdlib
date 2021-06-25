# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetInternalLinkType(BaseObject):
    """
    Returns information about the type of an internal link. Returns a 404 error if the link is not internal. Can be called before authorization
    
    Params:
        link (:class:`str`)
            The link
        
    """

    ID: str = Field("getInternalLinkType", alias="@type")
    link: str

    @staticmethod
    def read(q: dict) -> GetInternalLinkType:
        return GetInternalLinkType.construct(**q)
