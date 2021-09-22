# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .update import Update
from ..base_object import BaseObject


class Updates(BaseObject):
    """
    Contains a list of updates
    
    :param updates: List of updates
    :type updates: :class:`list[Update]`
    
    """

    ID: str = Field("updates", alias="@type")
    updates: list[Update]

    @staticmethod
    def read(q: dict) -> Updates:
        return Updates.construct(**q)
