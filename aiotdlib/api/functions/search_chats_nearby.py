# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    Location,
)


class SearchChatsNearby(BaseObject):
    """
    Returns a list of users and location-based supergroups nearby. The list of users nearby will be updated for 60 seconds after the request by the updates updateUsersNearby. The request must be sent again every 25 seconds with adjusted location to not miss new chats

    :param location: Current user location
    :type location: :class:`Location`
    """

    ID: typing.Literal["searchChatsNearby"] = "searchChatsNearby"
    location: Location
