# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetRecentlyVisitedTMeUrls(BaseObject):
    """
    Returns t.me URLs recently visited by a newly registered user
    
    Params:
        referrer (:class:`str`)
            Google Play referrer to identify the user
        
    """

    ID: str = Field("getRecentlyVisitedTMeUrls", alias="@type")
    referrer: str

    @staticmethod
    def read(q: dict) -> GetRecentlyVisitedTMeUrls:
        return GetRecentlyVisitedTMeUrls.construct(**q)
