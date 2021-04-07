# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RemoveRecentHashtag(BaseObject):
    """
    Removes a hashtag from the list of recently used hashtags
    
    Params:
        hashtag (:class:`str`)
            Hashtag to delete
        
    """

    ID: str = Field("removeRecentHashtag", alias="@type")
    hashtag: str

    @staticmethod
    def read(q: dict) -> RemoveRecentHashtag:
        return RemoveRecentHashtag.construct(**q)
