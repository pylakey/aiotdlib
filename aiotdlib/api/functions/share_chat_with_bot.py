# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ShareChatWithBot(BaseObject):
    """
    Shares a chat after pressing a keyboardButtonTypeRequestChat button with the bot

    :param chat_id: Identifier of the chat with the bot
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message with the button
    :type message_id: :class:`Int53`
    :param button_id: Identifier of the button
    :type button_id: :class:`Int32`
    :param shared_chat_id: Identifier of the shared chat
    :type shared_chat_id: :class:`Int53`
    :param only_check: Pass true to check that the chat can be shared by the button instead of actually sharing it. Doesn't check bot_is_member and bot_administrator_rights restrictions. If the bot must be a member, then all chats from getGroupsInCommon and all chats, where the user can add the bot, are suitable. In the latter case the bot will be automatically added to the chat. If the bot must be an administrator, then all chats, where the bot already has requested rights or can be added to administrators by the user, are suitable. In the latter case the bot will be automatically granted requested rights
    :type only_check: :class:`Bool`
    """

    ID: typing.Literal["shareChatWithBot"] = "shareChatWithBot"
    chat_id: Int53
    message_id: Int53
    button_id: Int32
    shared_chat_id: Int53
    only_check: Bool = False
