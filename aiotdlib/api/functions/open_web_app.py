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
    MessageReplyTo,
    ThemeParameters,
)


class OpenWebApp(BaseObject):
    """
    Informs TDLib that a Web App is being opened from the attachment menu, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an inlineKeyboardButtonTypeWebApp button. For each bot, a confirmation alert about data sent to the bot must be shown once

    :param chat_id: Identifier of the chat in which the Web App is opened. The Web App can't be opened in secret chats
    :type chat_id: :class:`Int53`
    :param bot_user_id: Identifier of the bot, providing the Web App
    :type bot_user_id: :class:`Int53`
    :param url: The URL from an inlineKeyboardButtonTypeWebApp button, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an empty string otherwise
    :type url: :class:`String`
    :param application_name: Short name of the application; 0-64 English letters, digits, and underscores
    :type application_name: :class:`String`
    :param message_thread_id: If not 0, a message thread identifier in which the message will be sent
    :type message_thread_id: :class:`Int53`
    :param theme: Preferred Web App theme; pass null to use the default theme, defaults to None
    :type theme: :class:`ThemeParameters`, optional
    :param reply_to: Identifier of the replied message or story for the message sent by the Web App; pass null if none, defaults to None
    :type reply_to: :class:`MessageReplyTo`, optional
    """

    ID: typing.Literal["openWebApp"] = "openWebApp"
    chat_id: Int53
    bot_user_id: Int53
    url: String
    application_name: String
    message_thread_id: Int53 = 0
    theme: typing.Optional[ThemeParameters] = None
    reply_to: typing.Optional[MessageReplyTo] = None
