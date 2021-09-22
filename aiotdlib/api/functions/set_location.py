# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import Location
from ..base_object import BaseObject


class SetLocation(BaseObject):
    """
    Changes the location of the current user. Needs to be called if GetOption("is_location_visible") is true and location changes for more than 1 kilometer
    
    :param location: The new location of the user
    :type location: :class:`Location`
    
    """

    ID: str = Field("setLocation", alias="@type")
    location: Location

    @staticmethod
    def read(q: dict) -> SetLocation:
        return SetLocation.construct(**q)
