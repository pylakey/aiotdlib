# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Location(BaseObject):
    """
    Describes a location on planet Earth
    
    :param latitude: Latitude of the location in degrees; as defined by the sender
    :type latitude: :class:`float`
    
    :param longitude: Longitude of the location, in degrees; as defined by the sender
    :type longitude: :class:`float`
    
    :param horizontal_accuracy: The estimated horizontal accuracy of the location, in meters; as defined by the sender. 0 if unknown
    :type horizontal_accuracy: :class:`float`
    
    """

    ID: str = Field("location", alias="@type")
    latitude: float
    longitude: float
    horizontal_accuracy: float

    @staticmethod
    def read(q: dict) -> Location:
        return Location.construct(**q)
