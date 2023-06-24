# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RemoveRecentlyFoundChat(BaseObject):
    """
    Removes a chat from the list of recently found chats

    :param chat_id: Identifier of the chat to be removed
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["removeRecentlyFoundChat"] = "removeRecentlyFoundChat"
    chat_id: Int53
