# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ResendLoginEmailAddressCode(BaseObject):
    """
    Resends the login email address verification code
    """

    ID: typing.Literal["resendLoginEmailAddressCode"] = "resendLoginEmailAddressCode"
