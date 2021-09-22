# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChangeStickerSet(BaseObject):
    """
    Installs/uninstalls or activates/archives a sticker set
    
    :param set_id: Identifier of the sticker set
    :type set_id: :class:`int`
    
    :param is_installed: The new value of is_installed
    :type is_installed: :class:`bool`
    
    :param is_archived: The new value of is_archived. A sticker set can't be installed and archived simultaneously
    :type is_archived: :class:`bool`
    
    """

    ID: str = Field("changeStickerSet", alias="@type")
    set_id: int
    is_installed: bool
    is_archived: bool

    @staticmethod
    def read(q: dict) -> ChangeStickerSet:
        return ChangeStickerSet.construct(**q)
