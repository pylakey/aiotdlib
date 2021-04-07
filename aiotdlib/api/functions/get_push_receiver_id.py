# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetPushReceiverId(BaseObject):
    """
    Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification. Can be called synchronously
    
    Params:
        payload (:class:`str`)
            JSON-encoded push notification payload
        
    """

    ID: str = Field("getPushReceiverId", alias="@type")
    payload: str

    @staticmethod
    def read(q: dict) -> GetPushReceiverId:
        return GetPushReceiverId.construct(**q)
