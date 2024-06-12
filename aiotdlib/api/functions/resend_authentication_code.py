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


class ResendAuthenticationCode(BaseObject):
    """
    Resends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitCode, the next_code_type of the result is not null and the server-specified timeout has passed, or when the current authorization state is authorizationStateWaitEmailCode

    :param reason: Reason of code resending; pass null if unknown, defaults to None
    :type reason: :class:`ResendCodeReason`, optional
    """

    ID: typing.Literal["resendAuthenticationCode"] = Field(
        "resendAuthenticationCode", validation_alias="@type", alias="@type"
    )
    reason: typing.Optional[ResendCodeReason] = None
