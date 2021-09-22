# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class TerminateSession(BaseObject):
    """
    Terminates a session of the current user
    
    :param session_id: Session identifier
    :type session_id: :class:`int`
    
    """

    ID: str = Field("terminateSession", alias="@type")
    session_id: int

    @staticmethod
    def read(q: dict) -> TerminateSession:
        return TerminateSession.construct(**q)
