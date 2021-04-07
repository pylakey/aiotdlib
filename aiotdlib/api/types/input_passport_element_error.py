# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .input_passport_element_error_source import InputPassportElementErrorSource
from .passport_element_type import PassportElementType
from ..base_object import BaseObject


class InputPassportElementError(BaseObject):
    """
    Contains the description of an error in a Telegram Passport element; for bots only
    
    Params:
        type_ (:class:`PassportElementType`)
            Type of Telegram Passport element that has the error
        
        message (:class:`str`)
            Error message
        
        source (:class:`InputPassportElementErrorSource`)
            Error source
        
    """

    ID: str = Field("inputPassportElementError", alias="@type")
    type_: PassportElementType = Field(..., alias='type')
    message: str
    source: InputPassportElementErrorSource

    @staticmethod
    def read(q: dict) -> InputPassportElementError:
        return InputPassportElementError.construct(**q)
