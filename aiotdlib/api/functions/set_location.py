# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import Location


class SetLocation(BaseObject):
    """
    Changes the location of the current user. Needs to be called if GetOption("is_location_visible") is true and location changes for more than 1 kilometer
    
    Params:
        location (:class:`Location`)
            The new location of the user
        
    """

    ID: str = Field("setLocation", alias="@type")
    location: Location

    @staticmethod
    def read(q: dict) -> SetLocation:
        return SetLocation.construct(**q)
