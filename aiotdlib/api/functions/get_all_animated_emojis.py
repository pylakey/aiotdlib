# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetAllAnimatedEmojis(BaseObject):
    """
    Returns all emojis, which has a corresponding animated emoji
    
    """

    ID: str = Field("getAllAnimatedEmojis", alias="@type")

    @staticmethod
    def read(q: dict) -> GetAllAnimatedEmojis:
        return GetAllAnimatedEmojis.construct(**q)
