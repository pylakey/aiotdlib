# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputFile
from ..base_object import BaseObject


class RemoveRecentSticker(BaseObject):
    """
    Removes a sticker from the list of recently used stickers
    
    :param is_attached: Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers
    :type is_attached: :class:`bool`
    
    :param sticker: Sticker file to delete
    :type sticker: :class:`InputFile`
    
    """

    ID: str = Field("removeRecentSticker", alias="@type")
    is_attached: bool
    sticker: InputFile

    @staticmethod
    def read(q: dict) -> RemoveRecentSticker:
        return RemoveRecentSticker.construct(**q)
