# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    DeviceToken,
)


class RegisterDevice(BaseObject):
    """
    Registers the currently used device for receiving push notifications. Returns a globally unique identifier of the push notification subscription

    :param device_token: Device token
    :type device_token: :class:`DeviceToken`
    :param other_user_ids: List of user identifiers of other users currently using the application
    :type other_user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["registerDevice"] = "registerDevice"
    device_token: DeviceToken
    other_user_ids: Vector[Int53]
