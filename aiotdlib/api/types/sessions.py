# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .session import Session
from ..base_object import BaseObject


class Sessions(BaseObject):
    """
    Contains a list of sessions
    
    :param sessions: List of sessions
    :type sessions: :class:`list[Session]`
    
    :param inactive_session_ttl_days: Number of days of inactivity before sessions will automatically be terminated; 1-366 days
    :type inactive_session_ttl_days: :class:`int`
    
    """

    ID: str = Field("sessions", alias="@type")
    sessions: list[Session]
    inactive_session_ttl_days: int

    @staticmethod
    def read(q: dict) -> Sessions:
        return Sessions.construct(**q)
