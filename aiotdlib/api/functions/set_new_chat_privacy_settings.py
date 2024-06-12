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
    NewChatPrivacySettings,
)


class SetNewChatPrivacySettings(BaseObject):
    """
    Changes privacy settings for new chat creation; can be used only if getOption("can_set_new_chat_privacy_settings")

    :param settings: New settings
    :type settings: :class:`NewChatPrivacySettings`
    """

    ID: typing.Literal["setNewChatPrivacySettings"] = Field(
        "setNewChatPrivacySettings", validation_alias="@type", alias="@type"
    )
    settings: NewChatPrivacySettings
