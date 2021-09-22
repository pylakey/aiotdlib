# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetSupergroupFullInfo(BaseObject):
    """
    Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute
    
    :param supergroup_id: Supergroup or channel identifier
    :type supergroup_id: :class:`int`
    
    """

    ID: str = Field("getSupergroupFullInfo", alias="@type")
    supergroup_id: int

    @staticmethod
    def read(q: dict) -> GetSupergroupFullInfo:
        return GetSupergroupFullInfo.construct(**q)
