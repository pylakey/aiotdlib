# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import Location


class GetMapThumbnailFile(BaseObject):
    """
    Returns information about a file with a map thumbnail in PNG format. Only map thumbnail files with size less than 1MB can be downloaded
    
    :param location: Location of the map center
    :type location: :class:`Location`
    
    :param zoom: Map zoom level; 13-20
    :type zoom: :class:`int`
    
    :param width: Map width in pixels before applying scale; 16-1024
    :type width: :class:`int`
    
    :param height: Map height in pixels before applying scale; 16-1024
    :type height: :class:`int`
    
    :param scale: Map scale; 1-3
    :type scale: :class:`int`
    
    :param chat_id: Identifier of a chat in which the thumbnail will be shown. Use 0 if unknown
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getMapThumbnailFile", alias="@type")
    location: Location
    zoom: int
    width: int
    height: int
    scale: int
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetMapThumbnailFile:
        return GetMapThumbnailFile.construct(**q)
