# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputPassportElement
from ..base_object import BaseObject


class SetPassportElement(BaseObject):
    """
    Adds an element to the user's Telegram Passport. May return an error with a message "PHONE_VERIFICATION_NEEDED" or "EMAIL_VERIFICATION_NEEDED" if the chosen phone number or the chosen email address must be verified first
    
    :param element: Input Telegram Passport element
    :type element: :class:`InputPassportElement`
    
    :param password: Password of the current user
    :type password: :class:`str`
    
    """

    ID: str = Field("setPassportElement", alias="@type")
    element: InputPassportElement
    password: str

    @staticmethod
    def read(q: dict) -> SetPassportElement:
        return SetPassportElement.construct(**q)
