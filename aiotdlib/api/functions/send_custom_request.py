# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SendCustomRequest(BaseObject):
    """
    Sends a custom request; for bots only
    
    Params:
        method (:class:`str`)
            The method name
        
        parameters (:class:`str`)
            JSON-serialized method parameters
        
    """

    ID: str = Field("sendCustomRequest", alias="@type")
    method: str
    parameters: str

    @staticmethod
    def read(q: dict) -> SendCustomRequest:
        return SendCustomRequest.construct(**q)
