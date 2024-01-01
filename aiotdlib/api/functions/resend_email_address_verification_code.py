# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ResendEmailAddressVerificationCode(BaseObject):
    """
    Resends the code to verify an email address to be added to a user's Telegram Passport
    """

    ID: typing.Literal["resendEmailAddressVerificationCode"] = Field(
        "resendEmailAddressVerificationCode", validation_alias="@type", alias="@type"
    )
