# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckPhoneNumberConfirmationCode(BaseObject):
    """
    Checks phone number confirmation code

    :param code: Confirmation code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkPhoneNumberConfirmationCode"] = "checkPhoneNumberConfirmationCode"
    code: String
