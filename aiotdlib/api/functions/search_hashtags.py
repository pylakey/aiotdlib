# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SearchHashtags(BaseObject):
    """
    Searches for recently used hashtags by their prefix
    
    :param prefix: Hashtag prefix to search for
    :type prefix: :class:`str`
    
    :param limit: The maximum number of hashtags to be returned
    :type limit: :class:`int`
    
    """

    ID: str = Field("searchHashtags", alias="@type")
    prefix: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchHashtags:
        return SearchHashtags.construct(**q)
