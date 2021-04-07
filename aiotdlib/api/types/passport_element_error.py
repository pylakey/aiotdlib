# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .passport_element_error_source import PassportElementErrorSource
from .passport_element_type import PassportElementType
from ..base_object import BaseObject


class PassportElementError(BaseObject):
    """
    Contains the description of an error in a Telegram Passport element
    
    Params:
        type_ (:class:`PassportElementType`)
            Type of the Telegram Passport element which has the error
        
        message (:class:`str`)
            Error message
        
        source (:class:`PassportElementErrorSource`)
            Error source
        
    """

    ID: str = Field("passportElementError", alias="@type")
    type_: PassportElementType = Field(..., alias='type')
    message: str
    source: PassportElementErrorSource

    @staticmethod
    def read(q: dict) -> PassportElementError:
        return PassportElementError.construct(**q)
