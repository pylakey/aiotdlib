# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class KeyboardButtonType(BaseObject):
    """
    Describes a keyboard button type
    
    """

    ID: str = Field("keyboardButtonType", alias="@type")


class KeyboardButtonTypeRequestLocation(KeyboardButtonType):
    """
    A button that sends the user's location when pressed; available only in private chats
    
    """

    ID: str = Field("keyboardButtonTypeRequestLocation", alias="@type")

    @staticmethod
    def read(q: dict) -> KeyboardButtonTypeRequestLocation:
        return KeyboardButtonTypeRequestLocation.construct(**q)


class KeyboardButtonTypeRequestPhoneNumber(KeyboardButtonType):
    """
    A button that sends the user's phone number when pressed; available only in private chats
    
    """

    ID: str = Field("keyboardButtonTypeRequestPhoneNumber", alias="@type")

    @staticmethod
    def read(q: dict) -> KeyboardButtonTypeRequestPhoneNumber:
        return KeyboardButtonTypeRequestPhoneNumber.construct(**q)


class KeyboardButtonTypeRequestPoll(KeyboardButtonType):
    """
    A button that allows the user to create and send a poll when pressed; available only in private chats
    
    Params:
        force_regular (:class:`bool`)
            If true, only regular polls must be allowed to create
        
        force_quiz (:class:`bool`)
            If true, only polls in quiz mode must be allowed to create
        
    """

    ID: str = Field("keyboardButtonTypeRequestPoll", alias="@type")
    force_regular: bool
    force_quiz: bool

    @staticmethod
    def read(q: dict) -> KeyboardButtonTypeRequestPoll:
        return KeyboardButtonTypeRequestPoll.construct(**q)


class KeyboardButtonTypeText(KeyboardButtonType):
    """
    A simple button, with text that should be sent when the button is pressed
    
    """

    ID: str = Field("keyboardButtonTypeText", alias="@type")

    @staticmethod
    def read(q: dict) -> KeyboardButtonTypeText:
        return KeyboardButtonTypeText.construct(**q)
