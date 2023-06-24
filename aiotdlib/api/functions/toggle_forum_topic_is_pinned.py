# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleForumTopicIsPinned(BaseObject):
    """
    Changes the pinned state of a forum topic; requires can_manage_topics administrator right in the supergroup. There can be up to getOption("pinned_forum_topic_count_max") pinned forum topics

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`Int53`
    :param is_pinned: Pass true to pin the topic; pass false to unpin it
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["toggleForumTopicIsPinned"] = "toggleForumTopicIsPinned"
    chat_id: Int53
    message_thread_id: Int53
    is_pinned: Bool = False
