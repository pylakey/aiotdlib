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


class GetWebAppUrl(BaseObject):
    """
    Returns an HTTPS URL of a Web App to open from the side menu, a keyboardButtonTypeWebApp button, or an inlineQueryResultsButtonTypeWebApp button

    :param bot_user_id: Identifier of the target bot. If the bot is restricted for the current user, then show an error instead of calling the method
    :type bot_user_id: :class:`Int53`
    :param url: The URL from a keyboardButtonTypeWebApp button, inlineQueryResultsButtonTypeWebApp button, or an empty string when the bot is opened from the side menu
    :type url: :class:`String`
    :param parameters: Parameters to use to open the Web App
    :type parameters: :class:`WebAppOpenParameters`
    """

    ID: typing.Literal["getWebAppUrl"] = Field("getWebAppUrl", validation_alias="@type", alias="@type")
    bot_user_id: Int53
    url: String
    parameters: WebAppOpenParameters
