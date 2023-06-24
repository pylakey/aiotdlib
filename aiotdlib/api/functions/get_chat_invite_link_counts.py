# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatInviteLinkCounts(BaseObject):
    """
    Returns list of chat administrators with number of their invite links. Requires owner privileges in the chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatInviteLinkCounts"] = "getChatInviteLinkCounts"
    chat_id: Int53
