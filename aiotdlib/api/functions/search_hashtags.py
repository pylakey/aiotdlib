# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchHashtags(BaseObject):
    """
    Searches for recently used hashtags by their prefix
    
    Params:
        prefix (:class:`str`)
            Hashtag prefix to search for
        
        limit (:class:`int`)
            The maximum number of hashtags to be returned
        
    """

    ID: str = Field("searchHashtags", alias="@type")
    prefix: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchHashtags:
        return SearchHashtags.construct(**q)
