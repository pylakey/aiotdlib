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


class GetMapThumbnailFile(BaseObject):
    """
    Returns information about a file with a map thumbnail in PNG format. Only map thumbnail files with size less than 1MB can be downloaded

    :param location: Location of the map center
    :type location: :class:`Location`
    :param zoom: Map zoom level; 13-20
    :type zoom: :class:`Int32`
    :param width: Map width in pixels before applying scale; 16-1024
    :type width: :class:`Int32`
    :param height: Map height in pixels before applying scale; 16-1024
    :type height: :class:`Int32`
    :param scale: Map scale; 1-3
    :type scale: :class:`Int32`
    :param chat_id: Identifier of a chat in which the thumbnail will be shown. Use 0 if unknown
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getMapThumbnailFile"] = "getMapThumbnailFile"
    location: Location
    zoom: Int32
    width: Int32
    height: Int32
    scale: Int32
    chat_id: Int53
