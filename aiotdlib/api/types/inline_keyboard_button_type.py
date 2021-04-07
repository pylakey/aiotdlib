# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class InlineKeyboardButtonType(BaseObject):
    """
    Describes the type of an inline keyboard button
    
    """

    ID: str = Field("inlineKeyboardButtonType", alias="@type")


class InlineKeyboardButtonTypeBuy(InlineKeyboardButtonType):
    """
    A button to buy something. This button must be in the first column and row of the keyboard and can be attached only to a message with content of the type messageInvoice
    
    """

    ID: str = Field("inlineKeyboardButtonTypeBuy", alias="@type")

    @staticmethod
    def read(q: dict) -> InlineKeyboardButtonTypeBuy:
        return InlineKeyboardButtonTypeBuy.construct(**q)


class InlineKeyboardButtonTypeCallback(InlineKeyboardButtonType):
    """
    A button that sends a callback query to a bot
    
    Params:
        data (:class:`str`)
            Data to be sent to the bot via a callback query
        
    """

    ID: str = Field("inlineKeyboardButtonTypeCallback", alias="@type")
    data: str

    @staticmethod
    def read(q: dict) -> InlineKeyboardButtonTypeCallback:
        return InlineKeyboardButtonTypeCallback.construct(**q)


class InlineKeyboardButtonTypeCallbackGame(InlineKeyboardButtonType):
    """
    A button with a game that sends a callback query to a bot. This button must be in the first column and row of the keyboard and can be attached only to a message with content of the type messageGame
    
    """

    ID: str = Field("inlineKeyboardButtonTypeCallbackGame", alias="@type")

    @staticmethod
    def read(q: dict) -> InlineKeyboardButtonTypeCallbackGame:
        return InlineKeyboardButtonTypeCallbackGame.construct(**q)


class InlineKeyboardButtonTypeCallbackWithPassword(InlineKeyboardButtonType):
    """
    A button that asks for password of the current user and then sends a callback query to a bot
    
    Params:
        data (:class:`str`)
            Data to be sent to the bot via a callback query
        
    """

    ID: str = Field("inlineKeyboardButtonTypeCallbackWithPassword", alias="@type")
    data: str

    @staticmethod
    def read(q: dict) -> InlineKeyboardButtonTypeCallbackWithPassword:
        return InlineKeyboardButtonTypeCallbackWithPassword.construct(**q)


class InlineKeyboardButtonTypeLoginUrl(InlineKeyboardButtonType):
    """
    A button that opens a specified URL and automatically authorize the current user if allowed to do so
    
    Params:
        url (:class:`str`)
            An HTTP URL to open
        
        id (:class:`int`)
            Unique button identifier
        
        forward_text (:class:`str`)
            If non-empty, new text of the button in forwarded messages
        
    """

    ID: str = Field("inlineKeyboardButtonTypeLoginUrl", alias="@type")
    url: str
    id: int
    forward_text: str

    @staticmethod
    def read(q: dict) -> InlineKeyboardButtonTypeLoginUrl:
        return InlineKeyboardButtonTypeLoginUrl.construct(**q)


class InlineKeyboardButtonTypeSwitchInline(InlineKeyboardButtonType):
    """
    A button that forces an inline query to the bot to be inserted in the input field
    
    Params:
        query (:class:`str`)
            Inline query to be sent to the bot
        
        in_current_chat (:class:`bool`)
            True, if the inline query should be sent from the current chat
        
    """

    ID: str = Field("inlineKeyboardButtonTypeSwitchInline", alias="@type")
    query: str
    in_current_chat: bool

    @staticmethod
    def read(q: dict) -> InlineKeyboardButtonTypeSwitchInline:
        return InlineKeyboardButtonTypeSwitchInline.construct(**q)


class InlineKeyboardButtonTypeUrl(InlineKeyboardButtonType):
    """
    A button that opens a specified URL
    
    Params:
        url (:class:`str`)
            HTTP or tg:// URL to open
        
    """

    ID: str = Field("inlineKeyboardButtonTypeUrl", alias="@type")
    url: str

    @staticmethod
    def read(q: dict) -> InlineKeyboardButtonTypeUrl:
        return InlineKeyboardButtonTypeUrl.construct(**q)
