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
    ReactionNotificationSettings,
)


class SetReactionNotificationSettings(BaseObject):
    """
    Changes notification settings for reactions

    :param notification_settings: The new notification settings for reactions
    :type notification_settings: :class:`ReactionNotificationSettings`
    """

    ID: typing.Literal["setReactionNotificationSettings"] = Field(
        "setReactionNotificationSettings", validation_alias="@type", alias="@type"
    )
    notification_settings: ReactionNotificationSettings
