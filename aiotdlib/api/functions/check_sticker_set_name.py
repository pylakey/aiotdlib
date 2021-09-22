# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CheckStickerSetName(BaseObject):
    """
    Checks whether a name can be used for a new sticker set
    
    :param name: Name to be checked
    :type name: :class:`str`
    
    """

    ID: str = Field("checkStickerSetName", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> CheckStickerSetName:
        return CheckStickerSetName.construct(**q)
