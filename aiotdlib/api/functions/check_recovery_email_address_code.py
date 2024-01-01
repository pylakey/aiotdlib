# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckRecoveryEmailAddressCode(BaseObject):
    """
    Checks the 2-step verification recovery email address verification code

    :param code: Verification code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkRecoveryEmailAddressCode"] = Field(
        "checkRecoveryEmailAddressCode", validation_alias="@type", alias="@type"
    )
    code: String
