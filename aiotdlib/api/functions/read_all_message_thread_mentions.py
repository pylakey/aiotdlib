# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReadAllMessageThreadMentions(BaseObject):
    """
    Marks all mentions in a forum topic as read

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_thread_id: Message thread identifier in which mentions are marked as read
    :type message_thread_id: :class:`Int53`
    """

    ID: typing.Literal["readAllMessageThreadMentions"] = "readAllMessageThreadMentions"
    chat_id: Int53
    message_thread_id: Int53
