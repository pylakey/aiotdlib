# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RemoveBackground(BaseObject):
    """
    Removes background from the list of installed backgrounds
    
    Params:
        background_id (:class:`int`)
            The background identifier
        
    """

    ID: str = Field("removeBackground", alias="@type")
    background_id: int

    @staticmethod
    def read(q: dict) -> RemoveBackground:
        return RemoveBackground.construct(**q)
