# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleSessionCanAcceptCalls(BaseObject):
    """
    Toggles whether a session can accept incoming calls
    
    :param session_id: Session identifier
    :type session_id: :class:`int`
    
    :param can_accept_calls: Pass true to allow accepting incoming calls by the session; pass false otherwise
    :type can_accept_calls: :class:`bool`
    
    """

    ID: str = Field("toggleSessionCanAcceptCalls", alias="@type")
    session_id: int
    can_accept_calls: bool

    @staticmethod
    def read(q: dict) -> ToggleSessionCanAcceptCalls:
        return ToggleSessionCanAcceptCalls.construct(**q)
