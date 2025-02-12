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
    WebAppOpenParameters,
)


class GetMainWebApp(BaseObject):
    """
    Returns information needed to open the main Web App of a bot

    :param bot_user_id: Identifier of the target bot. If the bot is restricted for the current user, then show an error instead of calling the method
    :type bot_user_id: :class:`Int53`
    :param start_parameter: Start parameter from internalLinkTypeMainWebApp
    :type start_parameter: :class:`String`
    :param parameters: Parameters to use to open the Web App
    :type parameters: :class:`WebAppOpenParameters`
    :param chat_id: Identifier of the chat in which the Web App is opened; pass 0 if none
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getMainWebApp"] = Field("getMainWebApp", validation_alias="@type", alias="@type")
    bot_user_id: Int53
    start_parameter: String
    parameters: WebAppOpenParameters
    chat_id: Int53 = 0
