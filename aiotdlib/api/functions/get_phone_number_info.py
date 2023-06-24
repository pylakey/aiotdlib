# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPhoneNumberInfo(BaseObject):
    """
    Returns information about a phone number by its prefix. Can be called before authorization

    :param phone_number_prefix: The phone number prefix
    :type phone_number_prefix: :class:`String`
    """

    ID: typing.Literal["getPhoneNumberInfo"] = "getPhoneNumberInfo"
    phone_number_prefix: String
