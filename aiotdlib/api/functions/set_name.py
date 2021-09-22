# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetName(BaseObject):
    """
    Changes the first and last name of the current user
    
    :param first_name: The new value of the first name for the current user; 1-64 characters
    :type first_name: :class:`str`
    
    :param last_name: The new value of the optional last name for the current user; 0-64 characters, defaults to None
    :type last_name: :class:`str`, optional
    
    """

    ID: str = Field("setName", alias="@type")
    first_name: str = Field(..., min_length=1, max_length=64)
    last_name: typing.Optional[str] = Field(None, max_length=64)

    @staticmethod
    def read(q: dict) -> SetName:
        return SetName.construct(**q)
