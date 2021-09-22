# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GroupCallVideoSourceGroup(BaseObject):
    """
    Describes a group of video synchronization source identifiers
    
    :param semantics: The semantics of sources, one of "SIM" or "FID"
    :type semantics: :class:`str`
    
    :param source_ids: The list of synchronization source identifiers
    :type source_ids: :class:`list[int]`
    
    """

    ID: str = Field("groupCallVideoSourceGroup", alias="@type")
    semantics: str
    source_ids: list[int]

    @staticmethod
    def read(q: dict) -> GroupCallVideoSourceGroup:
        return GroupCallVideoSourceGroup.construct(**q)
