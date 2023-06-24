# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetPinnedForumTopics(BaseObject):
    """
    Changes the order of pinned forum topics

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_thread_ids: The new list of pinned forum topics
    :type message_thread_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["setPinnedForumTopics"] = "setPinnedForumTopics"
    chat_id: Int53
    message_thread_ids: Vector[Int53]
