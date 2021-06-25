# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GroupCallVideoSourceGroup(BaseObject):
    """
    Describes a group of video synchronization source identifiers
    
    Params:
        semantics (:class:`str`)
            The semantics of sources, one of "SIM" or "FID"
        
        source_ids (:obj:`list[int]`)
            The list of synchronization source identifiers
        
    """

    ID: str = Field("groupCallVideoSourceGroup", alias="@type")
    semantics: str
    source_ids: list[int]

    @staticmethod
    def read(q: dict) -> GroupCallVideoSourceGroup:
        return GroupCallVideoSourceGroup.construct(**q)
