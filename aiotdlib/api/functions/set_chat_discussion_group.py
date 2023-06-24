# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetChatDiscussionGroup(BaseObject):
    """
    Changes the discussion group of a channel chat; requires can_change_info administrator right in the channel if it is specified

    :param chat_id: Identifier of the channel chat. Pass 0 to remove a link from the supergroup passed in the second argument to a linked channel chat (requires can_pin_messages rights in the supergroup)
    :type chat_id: :class:`Int53`
    :param discussion_chat_id: Identifier of a new channel's discussion group. Use 0 to remove the discussion group. Use the method getSuitableDiscussionChats to find all suitable groups. Basic group chats must be first upgraded to supergroup chats. If new chat members don't have access to old messages in the supergroup, then toggleSupergroupIsAllHistoryAvailable must be used first to change that
    :type discussion_chat_id: :class:`Int53`
    """

    ID: typing.Literal["setChatDiscussionGroup"] = "setChatDiscussionGroup"
    chat_id: Int53
    discussion_chat_id: Int53
