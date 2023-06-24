# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckPasswordRecoveryCode(BaseObject):
    """
    Checks whether a 2-step verification password recovery code sent to an email address is valid

    :param recovery_code: Recovery code to check
    :type recovery_code: :class:`String`
    """

    ID: typing.Literal["checkPasswordRecoveryCode"] = "checkPasswordRecoveryCode"
    recovery_code: String
