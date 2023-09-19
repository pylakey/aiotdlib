# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStoryNotificationSettingsExceptions(BaseObject):
    """
    Returns list of chats with non-default notification settings for stories
    """

    ID: typing.Literal["getStoryNotificationSettingsExceptions"] = "getStoryNotificationSettingsExceptions"
