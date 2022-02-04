# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .added_reaction import AddedReaction
from ..base_object import BaseObject


class AddedReactions(BaseObject):
    """
    Represents a list of reactions added to a message
    
    :param total_count: The total count of found reactions
    :type total_count: :class:`int`
    
    :param reactions: The list of added reactions
    :type reactions: :class:`list[AddedReaction]`
    
    :param next_offset: The offset for the next request. If empty, there are no more results
    :type next_offset: :class:`str`
    
    """

    ID: str = Field("addedReactions", alias="@type")
    total_count: int
    reactions: list[AddedReaction]
    next_offset: str

    @staticmethod
    def read(q: dict) -> AddedReactions:
        return AddedReactions.construct(**q)
