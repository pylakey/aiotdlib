# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TerminateAllOtherSessions(BaseObject):
    """
    Terminates all other sessions of the current user
    
    """

    ID: str = Field("terminateAllOtherSessions", alias="@type")

    @staticmethod
    def read(q: dict) -> TerminateAllOtherSessions:
        return TerminateAllOtherSessions.construct(**q)
