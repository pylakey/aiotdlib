# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .passport_element import PassportElement
from ..base_object import BaseObject


class PassportElements(BaseObject):
    """
    Contains information about saved Telegram Passport elements
    
    Params:
        elements (:obj:`list[PassportElement]`)
            Telegram Passport elements
        
    """

    ID: str = Field("passportElements", alias="@type")
    elements: list[PassportElement]

    @staticmethod
    def read(q: dict) -> PassportElements:
        return PassportElements.construct(**q)
