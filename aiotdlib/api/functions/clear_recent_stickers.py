# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ClearRecentStickers(BaseObject):
    """
    Clears the list of recently used stickers
    
    :param is_attached: Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers
    :type is_attached: :class:`bool`
    
    """

    ID: str = Field("clearRecentStickers", alias="@type")
    is_attached: bool

    @staticmethod
    def read(q: dict) -> ClearRecentStickers:
        return ClearRecentStickers.construct(**q)
