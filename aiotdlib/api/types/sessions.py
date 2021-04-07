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
    
    Params:
        sessions (:obj:`list[Session]`)
            List of sessions
        
    """

    ID: str = Field("sessions", alias="@type")
    sessions: list[Session]

    @staticmethod
    def read(q: dict) -> Sessions:
        return Sessions.construct(**q)
