# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .location import Location
from ..base_object import BaseObject


class Venue(BaseObject):
    """
    Describes a venue
    
    :param location: Venue location; as defined by the sender
    :type location: :class:`Location`
    
    :param title: Venue name; as defined by the sender
    :type title: :class:`str`
    
    :param address: Venue address; as defined by the sender
    :type address: :class:`str`
    
    :param provider: Provider of the venue database; as defined by the sender. Currently only "foursquare" and "gplaces" (Google Places) need to be supported
    :type provider: :class:`str`
    
    :param id: Identifier of the venue in the provider database; as defined by the sender
    :type id: :class:`str`
    
    :param type_: Type of the venue in the provider database; as defined by the sender
    :type type_: :class:`str`
    
    """

    ID: str = Field("venue", alias="@type")
    location: Location
    title: str
    address: str
    provider: str
    id: str
    type_: str = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> Venue:
        return Venue.construct(**q)
