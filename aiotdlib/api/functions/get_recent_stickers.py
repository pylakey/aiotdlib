# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetRecentStickers(BaseObject):
    """
    Returns a list of recently used stickers
    
    :param is_attached: Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers
    :type is_attached: :class:`bool`
    
    """

    ID: str = Field("getRecentStickers", alias="@type")
    is_attached: bool

    @staticmethod
    def read(q: dict) -> GetRecentStickers:
        return GetRecentStickers.construct(**q)
