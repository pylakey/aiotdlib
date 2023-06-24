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
    ThemeParameters,
)


class GetWebAppUrl(BaseObject):
    """
    Returns an HTTPS URL of a Web App to open after keyboardButtonTypeWebApp or inlineQueryResultsButtonTypeWebApp button is pressed

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param url: The URL from the keyboardButtonTypeWebApp or inlineQueryResultsButtonTypeWebApp button
    :type url: :class:`String`
    :param application_name: Short name of the application; 0-64 English letters, digits, and underscores
    :type application_name: :class:`String`
    :param theme: Preferred Web App theme; pass null to use the default theme, defaults to None
    :type theme: :class:`ThemeParameters`, optional
    """

    ID: typing.Literal["getWebAppUrl"] = "getWebAppUrl"
    bot_user_id: Int53
    url: String
    application_name: String
    theme: typing.Optional[ThemeParameters] = None
