# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .location import Location
from ..base_object import BaseObject


class Venue(BaseObject):
    """
    Describes a venue
    
    Params:
        location (:class:`Location`)
            Venue location; as defined by the sender
        
        title (:class:`str`)
            Venue name; as defined by the sender
        
        address (:class:`str`)
            Venue address; as defined by the sender
        
        provider (:class:`str`)
            Provider of the venue database; as defined by the sender. Currently only "foursquare" and "gplaces" (Google Places) need to be supported
        
        id (:class:`str`)
            Identifier of the venue in the provider database; as defined by the sender
        
        type_ (:class:`str`)
            Type of the venue in the provider database; as defined by the sender
        
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
