# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .passport_suitable_element import PassportSuitableElement
from ..base_object import BaseObject


class PassportRequiredElement(BaseObject):
    """
    Contains a description of the required Telegram Passport element that was requested by a service
    
    :param suitable_elements: List of Telegram Passport elements any of which is enough to provide
    :type suitable_elements: :class:`list[PassportSuitableElement]`
    
    """

    ID: str = Field("passportRequiredElement", alias="@type")
    suitable_elements: list[PassportSuitableElement]

    @staticmethod
    def read(q: dict) -> PassportRequiredElement:
        return PassportRequiredElement.construct(**q)
