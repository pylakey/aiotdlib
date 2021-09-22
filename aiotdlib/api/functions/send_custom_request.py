# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SendCustomRequest(BaseObject):
    """
    Sends a custom request; for bots only
    
    :param method: The method name
    :type method: :class:`str`
    
    :param parameters: JSON-serialized method parameters
    :type parameters: :class:`str`
    
    """

    ID: str = Field("sendCustomRequest", alias="@type")
    method: str
    parameters: str

    @staticmethod
    def read(q: dict) -> SendCustomRequest:
        return SendCustomRequest.construct(**q)
