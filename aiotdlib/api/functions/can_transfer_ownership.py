# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CanTransferOwnership(BaseObject):
    """
    Checks whether the current session can be used to transfer a chat ownership to another user
    
    """

    ID: str = Field("canTransferOwnership", alias="@type")

    @staticmethod
    def read(q: dict) -> CanTransferOwnership:
        return CanTransferOwnership.construct(**q)
