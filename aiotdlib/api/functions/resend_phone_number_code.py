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
    ResendCodeReason,
)


class ResendPhoneNumberCode(BaseObject):
    """
    Resends the authentication code sent to a phone number. Works only if the previously received authenticationCodeInfo next_code_type was not null and the server-specified timeout has passed

    :param reason: Reason of code resending; pass null if unknown, defaults to None
    :type reason: :class:`ResendCodeReason`, optional
    """

    ID: typing.Literal["resendPhoneNumberCode"] = Field(
        "resendPhoneNumberCode", validation_alias="@type", alias="@type"
    )
    reason: typing.Optional[ResendCodeReason] = None
