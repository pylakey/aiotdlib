# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import PassportElementType


class GetPassportElement(BaseObject):
    """
    Returns one of the available Telegram Passport elements
    
    Params:
        type_ (:class:`PassportElementType`)
            Telegram Passport element type
        
        password (:class:`str`)
            Password of the current user
        
    """

    ID: str = Field("getPassportElement", alias="@type")
    type_: PassportElementType = Field(..., alias='type')
    password: str

    @staticmethod
    def read(q: dict) -> GetPassportElement:
        return GetPassportElement.construct(**q)
