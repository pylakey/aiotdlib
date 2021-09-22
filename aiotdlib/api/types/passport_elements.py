# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .passport_element import PassportElement
from ..base_object import BaseObject


class PassportElements(BaseObject):
    """
    Contains information about saved Telegram Passport elements
    
    :param elements: Telegram Passport elements
    :type elements: :class:`list[PassportElement]`
    
    """

    ID: str = Field("passportElements", alias="@type")
    elements: list[PassportElement]

    @staticmethod
    def read(q: dict) -> PassportElements:
        return PassportElements.construct(**q)
