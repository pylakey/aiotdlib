# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .update import Update
from ..base_object import BaseObject


class Updates(BaseObject):
    """
    Contains a list of updates
    
    Params:
        updates (:obj:`list[Update]`)
            List of updates
        
    """

    ID: str = Field("updates", alias="@type")
    updates: list[Update]

    @staticmethod
    def read(q: dict) -> Updates:
        return Updates.construct(**q)
