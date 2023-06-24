# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckAuthenticationBotToken(BaseObject):
    """
    Checks the authentication token of a bot; to log in as a bot. Works only when the current authorization state is authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in

    :param token: The bot token
    :type token: :class:`String`
    """

    ID: typing.Literal["checkAuthenticationBotToken"] = "checkAuthenticationBotToken"
    token: String
