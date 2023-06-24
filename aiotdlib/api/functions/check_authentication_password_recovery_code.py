# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckAuthenticationPasswordRecoveryCode(BaseObject):
    """
    Checks whether a 2-step verification password recovery code sent to an email address is valid. Works only when the current authorization state is authorizationStateWaitPassword

    :param recovery_code: Recovery code to check
    :type recovery_code: :class:`String`
    """

    ID: typing.Literal["checkAuthenticationPasswordRecoveryCode"] = "checkAuthenticationPasswordRecoveryCode"
    recovery_code: String
