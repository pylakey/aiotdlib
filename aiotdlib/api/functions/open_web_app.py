# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ThemeParameters


class OpenWebApp(BaseObject):
    """
    Informs TDLib that a Web App is being opened from attachment menu, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an inlineKeyboardButtonTypeWebApp button. For each bot, a confirmation alert about data sent to the bot must be shown once
    
    :param chat_id: Identifier of the chat in which the Web App is opened
    :type chat_id: :class:`int`
    
    :param bot_user_id: Identifier of the bot, providing the Web App
    :type bot_user_id: :class:`int`
    
    :param url: The URL from an inlineKeyboardButtonTypeWebApp button, a botMenuButton button, or an internalLinkTypeAttachmentMenuBot link, or an empty string otherwise
    :type url: :class:`str`
    
    :param theme: Preferred Web App theme; pass null to use the default theme
    :type theme: :class:`ThemeParameters`
    
    :param reply_to_message_id: Identifier of the replied message for the message sent by the Web App; 0 if none
    :type reply_to_message_id: :class:`int`
    
    """

    ID: str = Field("openWebApp", alias="@type")
    chat_id: int
    bot_user_id: int
    url: str
    theme: ThemeParameters
    reply_to_message_id: int

    @staticmethod
    def read(q: dict) -> OpenWebApp:
        return OpenWebApp.construct(**q)
