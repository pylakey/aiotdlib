# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .keyboard_button_type import KeyboardButtonType
from ..base_object import BaseObject


class KeyboardButton(BaseObject):
    """
    Represents a single button in a bot keyboard
    
    :param text: Text of the button
    :type text: :class:`str`
    
    :param type_: Type of the button
    :type type_: :class:`KeyboardButtonType`
    
    """

    ID: str = Field("keyboardButton", alias="@type")
    text: str
    type_: KeyboardButtonType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> KeyboardButton:
        return KeyboardButton.construct(**q)
