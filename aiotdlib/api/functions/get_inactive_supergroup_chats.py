# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetInactiveSupergroupChats(BaseObject):
    """
    Returns a list of recently inactive supergroups and channels. Can be used when user reaches limit on the number of joined supergroups and channels and receives CHANNELS_TOO_MUCH error
    
    """

    ID: str = Field("getInactiveSupergroupChats", alias="@type")

    @staticmethod
    def read(q: dict) -> GetInactiveSupergroupChats:
        return GetInactiveSupergroupChats.construct(**q)
