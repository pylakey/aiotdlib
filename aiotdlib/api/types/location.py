# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Location(BaseObject):
    """
    Describes a location on planet Earth
    
    Params:
        latitude (:class:`float`)
            Latitude of the location in degrees; as defined by the sender
        
        longitude (:class:`float`)
            Longitude of the location, in degrees; as defined by the sender
        
        horizontal_accuracy (:class:`float`)
            The estimated horizontal accuracy of the location, in meters; as defined by the sender. 0 if unknown
        
    """

    ID: str = Field("location", alias="@type")
    latitude: float
    longitude: float
    horizontal_accuracy: float

    @staticmethod
    def read(q: dict) -> Location:
        return Location.construct(**q)
