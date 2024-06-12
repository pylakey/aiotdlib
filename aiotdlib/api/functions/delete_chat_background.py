# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteChatBackground(BaseObject):
    """
    Deletes background in a specific chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param restore_previous: Pass true to restore previously set background. Can be used only in private and secret chats with non-deleted users if userFullInfo.set_chat_background == true. Supposed to be used from messageChatSetBackground messages with the currently set background that was set for both sides by the other user
    :type restore_previous: :class:`Bool`
    """

    ID: typing.Literal["deleteChatBackground"] = Field("deleteChatBackground", validation_alias="@type", alias="@type")
    chat_id: Int53
    restore_previous: Bool = False
