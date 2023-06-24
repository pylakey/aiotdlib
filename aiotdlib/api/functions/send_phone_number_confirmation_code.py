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


class SendPhoneNumberConfirmationCode(BaseObject):
    """
    Sends phone number confirmation code to handle links of the type internalLinkTypePhoneNumberConfirmation

    :param hash_: Hash value from the link
    :type hash_: :class:`String`
    :param phone_number: Phone number value from the link
    :type phone_number: :class:`String`
    :param settings: Settings for the authentication of the user's phone number; pass null to use default settings, defaults to None
    :type settings: :class:`PhoneNumberAuthenticationSettings`, optional
    """

    ID: typing.Literal["sendPhoneNumberConfirmationCode"] = "sendPhoneNumberConfirmationCode"
    hash_: String = Field(..., alias="hash")
    phone_number: String
    settings: typing.Optional[PhoneNumberAuthenticationSettings] = None
