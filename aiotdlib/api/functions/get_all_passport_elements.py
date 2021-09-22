# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetAllPassportElements(BaseObject):
    """
    Returns all available Telegram Passport elements
    
    :param password: Password of the current user
    :type password: :class:`str`
    
    """

    ID: str = Field("getAllPassportElements", alias="@type")
    password: str

    @staticmethod
    def read(q: dict) -> GetAllPassportElements:
        return GetAllPassportElements.construct(**q)
