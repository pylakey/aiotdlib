# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckAuthenticationCode(BaseObject):
    """
    Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode

    :param code: Authentication code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkAuthenticationCode"] = "checkAuthenticationCode"
    code: String
