# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatPinnedMessage(BaseObject):
    """
    Returns information about a newest pinned message in the chat

    :param chat_id: Identifier of the chat the message belongs to
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatPinnedMessage"] = "getChatPinnedMessage"
    chat_id: Int53
