# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputPassportElement


class SetPassportElement(BaseObject):
    """
    Adds an element to the user's Telegram Passport. May return an error with a message "PHONE_VERIFICATION_NEEDED" or "EMAIL_VERIFICATION_NEEDED" if the chosen phone number or the chosen email address must be verified first
    
    Params:
        element (:class:`InputPassportElement`)
            Input Telegram Passport element
        
        password (:class:`str`)
            Password of the current user
        
    """

    ID: str = Field("setPassportElement", alias="@type")
    element: InputPassportElement
    password: str

    @staticmethod
    def read(q: dict) -> SetPassportElement:
        return SetPassportElement.construct(**q)
