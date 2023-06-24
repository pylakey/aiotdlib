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
    ChatNotificationSettings,
)


class SetForumTopicNotificationSettings(BaseObject):
    """
    Changes the notification settings of a forum topic

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`Int53`
    :param notification_settings: New notification settings for the forum topic. If the topic is muted for more than 366 days, it is considered to be muted forever
    :type notification_settings: :class:`ChatNotificationSettings`
    """

    ID: typing.Literal["setForumTopicNotificationSettings"] = "setForumTopicNotificationSettings"
    chat_id: Int53
    message_thread_id: Int53
    notification_settings: ChatNotificationSettings
