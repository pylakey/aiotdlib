# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckChangePhoneNumberCode(BaseObject):
    """
    Checks the authentication code sent to confirm a new phone number of the user

    :param code: Authentication code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkChangePhoneNumberCode"] = "checkChangePhoneNumberCode"
    code: String
