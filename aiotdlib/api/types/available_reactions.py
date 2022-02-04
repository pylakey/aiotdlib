# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AvailableReactions(BaseObject):
    """
    Represents a list of available reactions
    
    :param reactions: List of reactions
    :type reactions: :class:`list[str]`
    
    """

    ID: str = Field("availableReactions", alias="@type")
    reactions: list[str]

    @staticmethod
    def read(q: dict) -> AvailableReactions:
        return AvailableReactions.construct(**q)
