# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CallId(BaseObject):
    """
    Contains the call identifier
    
    :param id: Call identifier
    :type id: :class:`int`
    
    """

    ID: str = Field("callId", alias="@type")
    id: int

    @staticmethod
    def read(q: dict) -> CallId:
        return CallId.construct(**q)
