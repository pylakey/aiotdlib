# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RequestQrCodeAuthentication(BaseObject):
    """
    Requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitEmailAddress, authorizationStateWaitEmailCode, authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

    :param other_user_ids: List of user identifiers of other users currently using the application
    :type other_user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["requestQrCodeAuthentication"] = "requestQrCodeAuthentication"
    other_user_ids: Vector[Int53]
