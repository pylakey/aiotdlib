# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetBasicGroupFullInfo(BaseObject):
    """
    Returns full information about a basic group by its identifier
    
    Params:
        basic_group_id (:class:`int`)
            Basic group identifier
        
    """

    ID: str = Field("getBasicGroupFullInfo", alias="@type")
    basic_group_id: int

    @staticmethod
    def read(q: dict) -> GetBasicGroupFullInfo:
        return GetBasicGroupFullInfo.construct(**q)
