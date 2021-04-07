# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetImportedContactCount(BaseObject):
    """
    Returns the total number of imported contacts
    
    """

    ID: str = Field("getImportedContactCount", alias="@type")

    @staticmethod
    def read(q: dict) -> GetImportedContactCount:
        return GetImportedContactCount.construct(**q)
