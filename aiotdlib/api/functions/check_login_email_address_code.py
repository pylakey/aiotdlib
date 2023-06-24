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


class CheckLoginEmailAddressCode(BaseObject):
    """
    Checks the login email address authentication

    :param code: Email address authentication to check
    :type code: :class:`EmailAddressAuthentication`
    """

    ID: typing.Literal["checkLoginEmailAddressCode"] = "checkLoginEmailAddressCode"
    code: EmailAddressAuthentication
