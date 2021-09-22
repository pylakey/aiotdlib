# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import CallProtocol
from ..base_object import BaseObject


class AcceptCall(BaseObject):
    """
    Accepts an incoming call
    
    :param call_id: Call identifier
    :type call_id: :class:`int`
    
    :param protocol: Description of the call protocols supported by the application
    :type protocol: :class:`CallProtocol`
    
    """

    ID: str = Field("acceptCall", alias="@type")
    call_id: int
    protocol: CallProtocol

    @staticmethod
    def read(q: dict) -> AcceptCall:
        return AcceptCall.construct(**q)
