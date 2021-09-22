# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class RequestQrCodeAuthentication(BaseObject):
    """
    Requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword
    
    :param other_user_ids: List of user identifiers of other users currently using the application
    :type other_user_ids: :class:`list[int]`
    
    """

    ID: str = Field("requestQrCodeAuthentication", alias="@type")
    other_user_ids: list[int]

    @staticmethod
    def read(q: dict) -> RequestQrCodeAuthentication:
        return RequestQrCodeAuthentication.construct(**q)
