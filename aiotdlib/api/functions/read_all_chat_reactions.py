# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReadAllChatReactions(BaseObject):
    """
    Marks all reactions in a chat or a forum topic as read

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["readAllChatReactions"] = "readAllChatReactions"
    chat_id: Int53
