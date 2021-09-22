# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SearchBackground(BaseObject):
    """
    Searches for a background by its name
    
    :param name: The name of the background
    :type name: :class:`str`
    
    """

    ID: str = Field("searchBackground", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> SearchBackground:
        return SearchBackground.construct(**q)
