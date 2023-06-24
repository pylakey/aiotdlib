# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetForumTopicLink(BaseObject):
    """
    Returns an HTTPS link to a topic in a forum chat. This is an offline request

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`Int53`
    """

    ID: typing.Literal["getForumTopicLink"] = "getForumTopicLink"
    chat_id: Int53
    message_thread_id: Int53
