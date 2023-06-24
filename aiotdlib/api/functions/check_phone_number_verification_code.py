# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckPhoneNumberVerificationCode(BaseObject):
    """
    Checks the phone number verification code for Telegram Passport

    :param code: Verification code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkPhoneNumberVerificationCode"] = "checkPhoneNumberVerificationCode"
    code: String
