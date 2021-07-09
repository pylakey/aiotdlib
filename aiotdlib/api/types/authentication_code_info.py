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
    
    Params:
        phone_number (:class:`str`)
            A phone number that is being authenticated
        
        type_ (:class:`AuthenticationCodeType`)
            Describes the way the code was sent to the user
        
        next_type (:class:`AuthenticationCodeType`)
            Describes the way the next code will be sent to the user; may be null
        
        timeout (:class:`int`)
            Timeout before the code can be re-sent, in seconds
        
    """

    ID: str = Field("authenticationCodeInfo", alias="@type")
    phone_number: str
    type_: AuthenticationCodeType = Field(..., alias='type')
    next_type: typing.Optional[AuthenticationCodeType] = None
    timeout: int

    @staticmethod
    def read(q: dict) -> AuthenticationCodeInfo:
        return AuthenticationCodeInfo.construct(**q)
