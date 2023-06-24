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


class GetWebAppLinkUrl(BaseObject):
    """
    Returns an HTTPS URL of a Web App to open after a link of the type internalLinkTypeWebApp is clicked

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param web_app_short_name: Short name of the Web App
    :type web_app_short_name: :class:`String`
    :param start_parameter: Start parameter from internalLinkTypeWebApp
    :type start_parameter: :class:`String`
    :param application_name: Short name of the application; 0-64 English letters, digits, and underscores
    :type application_name: :class:`String`
    :param chat_id: Identifier of the chat in which the link was clicked; pass 0 if none
    :type chat_id: :class:`Int53`
    :param allow_write_access: Pass true if the current user allowed the bot to send them messages
    :type allow_write_access: :class:`Bool`
    :param theme: Preferred Web App theme; pass null to use the default theme, defaults to None
    :type theme: :class:`ThemeParameters`, optional
    """

    ID: typing.Literal["getWebAppLinkUrl"] = "getWebAppLinkUrl"
    bot_user_id: Int53
    web_app_short_name: String
    start_parameter: String
    application_name: String
    chat_id: Int53 = 0
    allow_write_access: Bool = False
    theme: typing.Optional[ThemeParameters] = None
