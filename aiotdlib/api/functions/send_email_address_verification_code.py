# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SendEmailAddressVerificationCode(BaseObject):
    """
    Sends a code to verify an email address to be added to a user's Telegram Passport

    :param email_address: Email address
    :type email_address: :class:`String`
    """

    ID: typing.Literal["sendEmailAddressVerificationCode"] = "sendEmailAddressVerificationCode"
    email_address: String
