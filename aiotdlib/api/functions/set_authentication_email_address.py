# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetAuthenticationEmailAddress(BaseObject):
    """
    Sets the email address of the user and sends an authentication code to the email address. Works only when the current authorization state is authorizationStateWaitEmailAddress

    :param email_address: The email address of the user
    :type email_address: :class:`String`
    """

    ID: typing.Literal["setAuthenticationEmailAddress"] = "setAuthenticationEmailAddress"
    email_address: String
