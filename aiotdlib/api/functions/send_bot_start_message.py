# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SendBotStartMessage(BaseObject):
    """
    Invites a bot to a chat (if it is not yet a member) and sends it the /start command. Bots can't be invited to a private chat other than the chat with the bot. Bots can't be invited to channels (although they can be added as admins) and secret chats. Returns the sent message

    :param bot_user_id: Identifier of the bot
    :type bot_user_id: :class:`Int53`
    :param chat_id: Identifier of the target chat
    :type chat_id: :class:`Int53`
    :param parameter: A hidden parameter sent to the bot for deep linking purposes (https://core.telegram.org/bots#deep-linking)
    :type parameter: :class:`String`
    """

    ID: typing.Literal["sendBotStartMessage"] = "sendBotStartMessage"
    bot_user_id: Int53
    chat_id: Int53
    parameter: String
