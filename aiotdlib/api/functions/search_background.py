# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchBackground(BaseObject):
    """
    Searches for a background by its name
    
    Params:
        name (:class:`str`)
            The name of the background
        
    """

    ID: str = Field("searchBackground", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> SearchBackground:
        return SearchBackground.construct(**q)
