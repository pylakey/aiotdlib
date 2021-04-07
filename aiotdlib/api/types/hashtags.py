# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Hashtags(BaseObject):
    """
    Contains a list of hashtags
    
    Params:
        hashtags (:obj:`list[str]`)
            A list of hashtags
        
    """

    ID: str = Field("hashtags", alias="@type")
    hashtags: list[str]

    @staticmethod
    def read(q: dict) -> Hashtags:
        return Hashtags.construct(**q)
