# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetRecentlyVisitedTMeUrls(BaseObject):
    """
    Returns t.me URLs recently visited by a newly registered user
    
    :param referrer: Google Play referrer to identify the user
    :type referrer: :class:`str`
    
    """

    ID: str = Field("getRecentlyVisitedTMeUrls", alias="@type")
    referrer: str

    @staticmethod
    def read(q: dict) -> GetRecentlyVisitedTMeUrls:
        return GetRecentlyVisitedTMeUrls.construct(**q)
