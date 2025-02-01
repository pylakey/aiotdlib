# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckWebAppFileDownload(BaseObject):
    """
    Checks whether a file can be downloaded and saved locally by Web App request

    :param bot_user_id: Identifier of the bot, providing the Web App
    :type bot_user_id: :class:`Int53`
    :param file_name: Name of the file
    :type file_name: :class:`String`
    :param url: URL of the file
    :type url: :class:`String`
    """

    ID: typing.Literal["checkWebAppFileDownload"] = Field(
        "checkWebAppFileDownload", validation_alias="@type", alias="@type"
    )
    bot_user_id: Int53
    file_name: String
    url: String
