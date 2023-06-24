# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ResendPhoneNumberVerificationCode(BaseObject):
    """
    Resends the code to verify a phone number to be added to a user's Telegram Passport
    """

    ID: typing.Literal["resendPhoneNumberVerificationCode"] = "resendPhoneNumberVerificationCode"
