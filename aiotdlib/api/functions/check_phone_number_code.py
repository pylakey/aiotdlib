# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckPhoneNumberCode(BaseObject):
    """
    Check the authentication code and completes the request for which the code was sent if appropriate

    :param code: Authentication code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkPhoneNumberCode"] = Field("checkPhoneNumberCode", validation_alias="@type", alias="@type")
    code: String
