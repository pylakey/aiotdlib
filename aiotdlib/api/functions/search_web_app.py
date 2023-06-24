# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchWebApp(BaseObject):
    """
    Returns information about a Web App by its short name. Returns a 404 error if the Web App is not found

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param web_app_short_name: Short name of the Web App
    :type web_app_short_name: :class:`String`
    """

    ID: typing.Literal["searchWebApp"] = "searchWebApp"
    bot_user_id: Int53
    web_app_short_name: String
