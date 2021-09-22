# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SendCallSignalingData(BaseObject):
    """
    Sends call signaling data
    
    :param call_id: Call identifier
    :type call_id: :class:`int`
    
    :param data: The data
    :type data: :class:`str`
    
    """

    ID: str = Field("sendCallSignalingData", alias="@type")
    call_id: int
    data: str

    @staticmethod
    def read(q: dict) -> SendCallSignalingData:
        return SendCallSignalingData.construct(**q)
