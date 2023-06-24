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
    PhoneNumberAuthenticationSettings,
)


class SendPhoneNumberVerificationCode(BaseObject):
    """
    Sends a code to verify a phone number to be added to a user's Telegram Passport

    :param phone_number: The phone number of the user, in international format
    :type phone_number: :class:`String`
    :param settings: Settings for the authentication of the user's phone number; pass null to use default settings, defaults to None
    :type settings: :class:`PhoneNumberAuthenticationSettings`, optional
    """

    ID: typing.Literal["sendPhoneNumberVerificationCode"] = "sendPhoneNumberVerificationCode"
    phone_number: String
    settings: typing.Optional[PhoneNumberAuthenticationSettings] = None
