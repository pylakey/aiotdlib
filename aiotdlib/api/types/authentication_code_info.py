# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .authentication_code_type import AuthenticationCodeType
from ..base_object import BaseObject


class AuthenticationCodeInfo(BaseObject):
    """
    Information about the authentication code that was sent
    
    :param phone_number: A phone number that is being authenticated
    :type phone_number: :class:`str`
    
    :param type_: Describes the way the code was sent to the user
    :type type_: :class:`AuthenticationCodeType`
    
    :param next_type: Describes the way the next code will be sent to the user; may be null, defaults to None
    :type next_type: :class:`AuthenticationCodeType`, optional
    
    :param timeout: Timeout before the code can be re-sent, in seconds
    :type timeout: :class:`int`
    
    """

    ID: str = Field("authenticationCodeInfo", alias="@type")
    phone_number: str
    type_: AuthenticationCodeType = Field(..., alias='type')
    next_type: typing.Optional[AuthenticationCodeType] = None
    timeout: int

    @staticmethod
    def read(q: dict) -> AuthenticationCodeInfo:
        return AuthenticationCodeInfo.construct(**q)
