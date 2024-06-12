# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReportAuthenticationCodeMissing(BaseObject):
    """
    Reports that authentication code wasn't delivered via SMS; for official mobile applications only. Works only when the current authorization state is authorizationStateWaitCode

    :param mobile_network_code: Current mobile network code
    :type mobile_network_code: :class:`String`
    """

    ID: typing.Literal["reportAuthenticationCodeMissing"] = Field(
        "reportAuthenticationCodeMissing", validation_alias="@type", alias="@type"
    )
    mobile_network_code: String
