# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetAnimatedEmoji(BaseObject):
    """
    Returns an animated emoji corresponding to a given emoji. Returns a 404 error if the emoji has no animated emoji
    
    :param emoji: The emoji
    :type emoji: :class:`str`
    
    """

    ID: str = Field("getAnimatedEmoji", alias="@type")
    emoji: str

    @staticmethod
    def read(q: dict) -> GetAnimatedEmoji:
        return GetAnimatedEmoji.construct(**q)
