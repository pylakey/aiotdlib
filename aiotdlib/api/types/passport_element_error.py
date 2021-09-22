# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .passport_element_error_source import PassportElementErrorSource
from .passport_element_type import PassportElementType
from ..base_object import BaseObject


class PassportElementError(BaseObject):
    """
    Contains the description of an error in a Telegram Passport element
    
    :param type_: Type of the Telegram Passport element which has the error
    :type type_: :class:`PassportElementType`
    
    :param message: Error message
    :type message: :class:`str`
    
    :param source: Error source
    :type source: :class:`PassportElementErrorSource`
    
    """

    ID: str = Field("passportElementError", alias="@type")
    type_: PassportElementType = Field(..., alias='type')
    message: str
    source: PassportElementErrorSource

    @staticmethod
    def read(q: dict) -> PassportElementError:
        return PassportElementError.construct(**q)
