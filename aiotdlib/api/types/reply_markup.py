# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .inline_keyboard_button import InlineKeyboardButton
from .keyboard_button import KeyboardButton
from ..base_object import BaseObject


class ReplyMarkup(BaseObject):
    """
    Contains a description of a custom keyboard and actions that can be done with it to quickly reply to bots
    
    """

    ID: str = Field("replyMarkup", alias="@type")


class ReplyMarkupForceReply(ReplyMarkup):
    """
    Instructs application to force a reply to this message
    
    Params:
        is_personal (:class:`bool`)
            True, if a forced reply must automatically be shown to the current user. For outgoing messages, specify true to show the forced reply only for the mentioned users and for the target user of a reply
        
        input_field_placeholder (:class:`str`)
            If non-empty, the placeholder to be shown in the input field when the reply is active; 0-64 characters
        
    """

    ID: str = Field("replyMarkupForceReply", alias="@type")
    is_personal: bool
    input_field_placeholder: typing.Optional[str] = Field(None, max_length=64)

    @staticmethod
    def read(q: dict) -> ReplyMarkupForceReply:
        return ReplyMarkupForceReply.construct(**q)


class ReplyMarkupInlineKeyboard(ReplyMarkup):
    """
    Contains an inline keyboard layout
    
    Params:
        rows (:obj:`list[list[InlineKeyboardButton]]`)
            A list of rows of inline keyboard buttons
        
    """

    ID: str = Field("replyMarkupInlineKeyboard", alias="@type")
    rows: list[list[InlineKeyboardButton]]

    @staticmethod
    def read(q: dict) -> ReplyMarkupInlineKeyboard:
        return ReplyMarkupInlineKeyboard.construct(**q)


class ReplyMarkupRemoveKeyboard(ReplyMarkup):
    """
    Instructs application to remove the keyboard once this message has been received. This kind of keyboard can't be received in an incoming message; instead, UpdateChatReplyMarkup with message_id == 0 will be sent
    
    Params:
        is_personal (:class:`bool`)
            True, if the keyboard is removed only for the mentioned users or the target user of a reply
        
    """

    ID: str = Field("replyMarkupRemoveKeyboard", alias="@type")
    is_personal: bool

    @staticmethod
    def read(q: dict) -> ReplyMarkupRemoveKeyboard:
        return ReplyMarkupRemoveKeyboard.construct(**q)


class ReplyMarkupShowKeyboard(ReplyMarkup):
    """
    Contains a custom keyboard layout to quickly reply to bots
    
    Params:
        rows (:obj:`list[list[KeyboardButton]]`)
            A list of rows of bot keyboard buttons
        
        resize_keyboard (:class:`bool`)
            True, if the application needs to resize the keyboard vertically
        
        one_time (:class:`bool`)
            True, if the application needs to hide the keyboard after use
        
        is_personal (:class:`bool`)
            True, if the keyboard must automatically be shown to the current user. For outgoing messages, specify true to show the keyboard only for the mentioned users and for the target user of a reply
        
        input_field_placeholder (:class:`str`)
            If non-empty, the placeholder to be shown in the input field when the keyboard is active; 0-64 characters
        
    """

    ID: str = Field("replyMarkupShowKeyboard", alias="@type")
    rows: list[list[KeyboardButton]]
    resize_keyboard: bool
    one_time: bool
    is_personal: bool
    input_field_placeholder: typing.Optional[str] = Field(None, max_length=64)

    @staticmethod
    def read(q: dict) -> ReplyMarkupShowKeyboard:
        return ReplyMarkupShowKeyboard.construct(**q)
