# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPassportAuthorizationFormAvailableElements(BaseObject):
    """
    Returns already available Telegram Passport elements suitable for completing a Telegram Passport authorization form. Result can be received only once for each authorization form

    :param authorization_form_id: Authorization form identifier
    :type authorization_form_id: :class:`Int32`
    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    """

    ID: typing.Literal[
        "getPassportAuthorizationFormAvailableElements"
    ] = "getPassportAuthorizationFormAvailableElements"
    authorization_form_id: Int32
    password: String
