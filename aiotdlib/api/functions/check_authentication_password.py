# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckAuthenticationPassword(BaseObject):
    """
    Checks the 2-step verification password for correctness. Works only when the current authorization state is authorizationStateWaitPassword

    :param password: The 2-step verification password to check
    :type password: :class:`String`
    """

    ID: typing.Literal["checkAuthenticationPassword"] = "checkAuthenticationPassword"
    password: String
