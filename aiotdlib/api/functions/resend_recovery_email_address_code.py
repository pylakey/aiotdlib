# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ResendRecoveryEmailAddressCode(BaseObject):
    """
    Resends the 2-step verification recovery email address verification code
    """

    ID: typing.Literal["resendRecoveryEmailAddressCode"] = "resendRecoveryEmailAddressCode"
