# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetUserProfilePhotos(BaseObject):
    """
    Returns the profile photos of a user. The result of this query may be outdated: some photos might have been deleted already
    
    Params:
        user_id (:class:`int`)
            User identifier
        
        offset (:class:`int`)
            The number of photos to skip; must be non-negative
        
        limit (:class:`int`)
            The maximum number of photos to be returned; up to 100
        
    """

    ID: str = Field("getUserProfilePhotos", alias="@type")
    user_id: int
    offset: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetUserProfilePhotos:
        return GetUserProfilePhotos.construct(**q)
