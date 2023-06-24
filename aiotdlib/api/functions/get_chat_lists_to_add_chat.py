# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatListsToAddChat(BaseObject):
    """
    Returns chat lists to which the chat can be added. This is an offline request

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatListsToAddChat"] = "getChatListsToAddChat"
    chat_id: Int53
