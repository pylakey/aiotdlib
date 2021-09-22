# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetSupergroup(BaseObject):
    """
    Returns information about a supergroup or a channel by its identifier. This is an offline request if the current user is not a bot
    
    :param supergroup_id: Supergroup or channel identifier
    :type supergroup_id: :class:`int`
    
    """

    ID: str = Field("getSupergroup", alias="@type")
    supergroup_id: int

    @staticmethod
    def read(q: dict) -> GetSupergroup:
        return GetSupergroup.construct(**q)
