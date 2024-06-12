# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReportPhoneNumberCodeMissing(BaseObject):
    """
    Reports that authentication code wasn't delivered via SMS to the specified phone number; for official mobile applications only

    :param mobile_network_code: Current mobile network code
    :type mobile_network_code: :class:`String`
    """

    ID: typing.Literal["reportPhoneNumberCodeMissing"] = Field(
        "reportPhoneNumberCodeMissing", validation_alias="@type", alias="@type"
    )
    mobile_network_code: String
