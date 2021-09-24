# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CheckStickerSetNameResult(BaseObject):
    """
    Represents result of checking whether a name can be used for a new sticker set
    
    """

    ID: str = Field("checkStickerSetNameResult", alias="@type")


class CheckStickerSetNameResultNameInvalid(CheckStickerSetNameResult):
    """
    The name is invalid
    
    """

    ID: str = Field("checkStickerSetNameResultNameInvalid", alias="@type")

    @staticmethod
    def read(q: dict) -> CheckStickerSetNameResultNameInvalid:
        return CheckStickerSetNameResultNameInvalid.construct(**q)


class CheckStickerSetNameResultNameOccupied(CheckStickerSetNameResult):
    """
    The name is occupied
    
    """

    ID: str = Field("checkStickerSetNameResultNameOccupied", alias="@type")

    @staticmethod
    def read(q: dict) -> CheckStickerSetNameResultNameOccupied:
        return CheckStickerSetNameResultNameOccupied.construct(**q)


class CheckStickerSetNameResultOk(CheckStickerSetNameResult):
    """
    The name can be set
    
    """

    ID: str = Field("checkStickerSetNameResultOk", alias="@type")

    @staticmethod
    def read(q: dict) -> CheckStickerSetNameResultOk:
        return CheckStickerSetNameResultOk.construct(**q)
