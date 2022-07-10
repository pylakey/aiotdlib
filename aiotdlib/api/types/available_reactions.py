# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .available_reaction import AvailableReaction
from ..base_object import BaseObject


class AvailableReactions(BaseObject):
    """
    Represents a list of available reactions
    
    :param reactions: List of reactions
    :type reactions: :class:`list[AvailableReaction]`
    
    """

    ID: str = Field("availableReactions", alias="@type")
    reactions: list[AvailableReaction]

    @staticmethod
    def read(q: dict) -> AvailableReactions:
        return AvailableReactions.construct(**q)
