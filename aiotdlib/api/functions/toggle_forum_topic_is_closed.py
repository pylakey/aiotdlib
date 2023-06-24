# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleForumTopicIsClosed(BaseObject):
    """
    Toggles whether a topic is closed in a forum supergroup chat; requires can_manage_topics administrator right in the supergroup unless the user is creator of the topic

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`Int53`
    :param is_closed: Pass true to close the topic; pass false to reopen it
    :type is_closed: :class:`Bool`
    """

    ID: typing.Literal["toggleForumTopicIsClosed"] = "toggleForumTopicIsClosed"
    chat_id: Int53
    message_thread_id: Int53
    is_closed: Bool = False
