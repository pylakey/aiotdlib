# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ResetAllNotificationSettings(BaseObject):
    """
    Resets all notification settings to their default values. By default, all chats are unmuted and message previews are shown
    """

    ID: typing.Literal["resetAllNotificationSettings"] = "resetAllNotificationSettings"
