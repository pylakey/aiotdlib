# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class PinChatMessage(BaseObject):
    """
    Pins a message in a chat; requires can_pin_messages rights or can_edit_messages rights in the channel

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the new pinned message
    :type message_id: :class:`Int53`
    :param disable_notification: Pass true to disable notification about the pinned message. Notifications are always disabled in channels and private chats
    :type disable_notification: :class:`Bool`
    :param only_for_self: Pass true to pin the message only for self; private chats only
    :type only_for_self: :class:`Bool`
    """

    ID: typing.Literal["pinChatMessage"] = "pinChatMessage"
    chat_id: Int53
    message_id: Int53
    disable_notification: Bool = False
    only_for_self: Bool = False
