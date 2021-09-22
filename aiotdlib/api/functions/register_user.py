# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class RegisterUser(BaseObject):
    """
    Finishes user registration. Works only when the current authorization state is authorizationStateWaitRegistration
    
    :param first_name: The first name of the user; 1-64 characters
    :type first_name: :class:`str`
    
    :param last_name: The last name of the user; 0-64 characters, defaults to None
    :type last_name: :class:`str`, optional
    
    """

    ID: str = Field("registerUser", alias="@type")
    first_name: str = Field(..., min_length=1, max_length=64)
    last_name: typing.Optional[str] = Field(None, max_length=64)

    @staticmethod
    def read(q: dict) -> RegisterUser:
        return RegisterUser.construct(**q)
