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
    
    Params:
        location (:class:`Location`)
            Location of the map center
        
        zoom (:class:`int`)
            Map zoom level; 13-20
        
        width (:class:`int`)
            Map width in pixels before applying scale; 16-1024
        
        height (:class:`int`)
            Map height in pixels before applying scale; 16-1024
        
        scale (:class:`int`)
            Map scale; 1-3
        
        chat_id (:class:`int`)
            Identifier of a chat, in which the thumbnail will be shown. Use 0 if unknown
        
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
