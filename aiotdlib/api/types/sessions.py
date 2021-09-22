# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .session import Session
from ..base_object import BaseObject


class Sessions(BaseObject):
    """
    Contains a list of sessions
    
    :param sessions: List of sessions
    :type sessions: :class:`list[Session]`
    
    """

    ID: str = Field("sessions", alias="@type")
    sessions: list[Session]

    @staticmethod
    def read(q: dict) -> Sessions:
        return Sessions.construct(**q)
