# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    ChatAvailableReactions,
)


class SetChatAvailableReactions(BaseObject):
    """
    Changes reactions, available in a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param available_reactions: Reactions available in the chat. All emoji reactions must be active
    :type available_reactions: :class:`ChatAvailableReactions`
    """

    ID: typing.Literal["setChatAvailableReactions"] = "setChatAvailableReactions"
    chat_id: Int53
    available_reactions: ChatAvailableReactions
