# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AddApplicationChangelog(BaseObject):
    """
    Adds server-provided application changelog as messages to the chat 777000 (Telegram) or as a stories; for official applications only. Returns a 404 error if nothing changed

    :param previous_application_version: The previous application version
    :type previous_application_version: :class:`String`
    """

    ID: typing.Literal["addApplicationChangelog"] = "addApplicationChangelog"
    previous_application_version: String
