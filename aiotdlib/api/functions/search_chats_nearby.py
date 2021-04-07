# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import Location


class SearchChatsNearby(BaseObject):
    """
    Returns a list of users and location-based supergroups nearby. The list of users nearby will be updated for 60 seconds after the request by the updates updateUsersNearby. The request should be sent again every 25 seconds with adjusted location to not miss new chats
    
    Params:
        location (:class:`Location`)
            Current user location
        
    """

    ID: str = Field("searchChatsNearby", alias="@type")
    location: Location

    @staticmethod
    def read(q: dict) -> SearchChatsNearby:
        return SearchChatsNearby.construct(**q)
