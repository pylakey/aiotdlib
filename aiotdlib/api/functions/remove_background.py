# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class RemoveBackground(BaseObject):
    """
    Removes background from the list of installed backgrounds
    
    :param background_id: The background identifier
    :type background_id: :class:`int`
    
    """

    ID: str = Field("removeBackground", alias="@type")
    background_id: int

    @staticmethod
    def read(q: dict) -> RemoveBackground:
        return RemoveBackground.construct(**q)
