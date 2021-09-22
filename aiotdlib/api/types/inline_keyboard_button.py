# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .inline_keyboard_button_type import InlineKeyboardButtonType
from ..base_object import BaseObject


class InlineKeyboardButton(BaseObject):
    """
    Represents a single button in an inline keyboard
    
    :param text: Text of the button
    :type text: :class:`str`
    
    :param type_: Type of the button
    :type type_: :class:`InlineKeyboardButtonType`
    
    """

    ID: str = Field("inlineKeyboardButton", alias="@type")
    text: str
    type_: InlineKeyboardButtonType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> InlineKeyboardButton:
        return InlineKeyboardButton.construct(**q)
