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
    NotificationSettingsScope,
)


class GetChatNotificationSettingsExceptions(BaseObject):
    """
    Returns list of chats with non-default notification settings for new messages

    :param compare_sound: Pass true to include in the response chats with only non-default sound
    :type compare_sound: :class:`Bool`
    :param scope: If specified, only chats from the scope will be returned; pass null to return chats from all scopes, defaults to None
    :type scope: :class:`NotificationSettingsScope`, optional
    """

    ID: typing.Literal["getChatNotificationSettingsExceptions"] = "getChatNotificationSettingsExceptions"
    compare_sound: Bool = False
    scope: typing.Optional[NotificationSettingsScope] = None
