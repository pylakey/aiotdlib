# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GroupCallId(BaseObject):
    """
    Contains the group call identifier
    
    :param id: Group call identifier
    :type id: :class:`int`
    
    """

    ID: str = Field("groupCallId", alias="@type")
    id: int

    @staticmethod
    def read(q: dict) -> GroupCallId:
        return GroupCallId.construct(**q)
