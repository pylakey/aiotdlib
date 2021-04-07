# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .inline_keyboard_button_type import InlineKeyboardButtonType
from ..base_object import BaseObject


class InlineKeyboardButton(BaseObject):
    """
    Represents a single button in an inline keyboard
    
    Params:
        text (:class:`str`)
            Text of the button
        
        type_ (:class:`InlineKeyboardButtonType`)
            Type of the button
        
    """

    ID: str = Field("inlineKeyboardButton", alias="@type")
    text: str
    type_: InlineKeyboardButtonType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> InlineKeyboardButton:
        return InlineKeyboardButton.construct(**q)
