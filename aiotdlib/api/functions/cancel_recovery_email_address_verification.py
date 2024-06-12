# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CancelRecoveryEmailAddressVerification(BaseObject):
    """
    Cancels verification of the 2-step verification recovery email address
    """

    ID: typing.Literal["cancelRecoveryEmailAddressVerification"] = Field(
        "cancelRecoveryEmailAddressVerification", validation_alias="@type", alias="@type"
    )
