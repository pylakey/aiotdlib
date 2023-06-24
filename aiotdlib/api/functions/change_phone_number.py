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


class ChangePhoneNumber(BaseObject):
    """
    Changes the phone number of the user and sends an authentication code to the user's new phone number; for official Android and iOS applications only. On success, returns information about the sent code

    :param phone_number: The new phone number of the user in international format
    :type phone_number: :class:`String`
    :param settings: Settings for the authentication of the user's phone number; pass null to use default settings, defaults to None
    :type settings: :class:`PhoneNumberAuthenticationSettings`, optional
    """

    ID: typing.Literal["changePhoneNumber"] = "changePhoneNumber"
    phone_number: String
    settings: typing.Optional[PhoneNumberAuthenticationSettings] = None
