# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import DeviceToken


class RegisterDevice(BaseObject):
    """
    Registers the currently used device for receiving push notifications. Returns a globally unique identifier of the push notification subscription
    
    Params:
        device_token (:class:`DeviceToken`)
            Device token
        
        other_user_ids (:obj:`list[int]`)
            List of user identifiers of other users currently using the application
        
    """

    ID: str = Field("registerDevice", alias="@type")
    device_token: DeviceToken
    other_user_ids: list[int]

    @staticmethod
    def read(q: dict) -> RegisterDevice:
        return RegisterDevice.construct(**q)
