# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetActiveSessions(BaseObject):
    """
    Returns all active sessions of the current user
    
    """

    ID: str = Field("getActiveSessions", alias="@type")

    @staticmethod
    def read(q: dict) -> GetActiveSessions:
        return GetActiveSessions.construct(**q)
