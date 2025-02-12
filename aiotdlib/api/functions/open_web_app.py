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
    InputMessageReplyTo,
    WebAppOpenParameters,
)


class OpenWebApp(BaseObject):
    """
    Informs TDLib that a Web App is being opened from the attachment menu, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an inlineKeyboardButtonTypeWebApp button. For each bot, a confirmation alert about data sent to the bot must be shown once

    :param chat_id: Identifier of the chat in which the Web App is opened. The Web App can't be opened in secret chats
    :type chat_id: :class:`Int53`
    :param bot_user_id: Identifier of the bot, providing the Web App. If the bot is restricted for the current user, then show an error instead of calling the method
    :type bot_user_id: :class:`Int53`
    :param url: The URL from an inlineKeyboardButtonTypeWebApp button, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an empty string otherwise
    :type url: :class:`String`
    :param parameters: Parameters to use to open the Web App
    :type parameters: :class:`WebAppOpenParameters`
    :param message_thread_id: If not 0, the message thread identifier in which the message will be sent
    :type message_thread_id: :class:`Int53`
    :param reply_to: Information about the message or story to be replied in the message sent by the Web App; pass null if none, defaults to None
    :type reply_to: :class:`InputMessageReplyTo`, optional
    """

    ID: typing.Literal["openWebApp"] = Field("openWebApp", validation_alias="@type", alias="@type")
    chat_id: Int53
    bot_user_id: Int53
    url: String
    parameters: WebAppOpenParameters
    message_thread_id: Int53 = 0
    reply_to: typing.Optional[InputMessageReplyTo] = None
