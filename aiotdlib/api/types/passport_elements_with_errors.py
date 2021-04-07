# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .passport_element import PassportElement
from .passport_element_error import PassportElementError
from ..base_object import BaseObject


class PassportElementsWithErrors(BaseObject):
    """
    Contains information about a Telegram Passport elements and corresponding errors
    
    Params:
        elements (:obj:`list[PassportElement]`)
            Telegram Passport elements
        
        errors (:obj:`list[PassportElementError]`)
            Errors in the elements that are already available
        
    """

    ID: str = Field("passportElementsWithErrors", alias="@type")
    elements: list[PassportElement]
    errors: list[PassportElementError]

    @staticmethod
    def read(q: dict) -> PassportElementsWithErrors:
        return PassportElementsWithErrors.construct(**q)
