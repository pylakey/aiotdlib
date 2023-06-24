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
    EmailAddressAuthentication,
)


class CheckAuthenticationEmailCode(BaseObject):
    """
    Checks the authentication of a email address. Works only when the current authorization state is authorizationStateWaitEmailCode

    :param code: Email address authentication to check
    :type code: :class:`EmailAddressAuthentication`
    """

    ID: typing.Literal["checkAuthenticationEmailCode"] = "checkAuthenticationEmailCode"
    code: EmailAddressAuthentication
