# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .passport_element import PassportElement
from .passport_element_error import PassportElementError
from ..base_object import BaseObject


class PassportElementsWithErrors(BaseObject):
    """
    Contains information about a Telegram Passport elements and corresponding errors
    
    :param elements: Telegram Passport elements
    :type elements: :class:`list[PassportElement]`
    
    :param errors: Errors in the elements that are already available
    :type errors: :class:`list[PassportElementError]`
    
    """

    ID: str = Field("passportElementsWithErrors", alias="@type")
    elements: list[PassportElement]
    errors: list[PassportElementError]

    @staticmethod
    def read(q: dict) -> PassportElementsWithErrors:
        return PassportElementsWithErrors.construct(**q)
