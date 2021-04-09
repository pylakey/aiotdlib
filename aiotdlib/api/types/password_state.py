# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .email_address_authentication_code_info import EmailAddressAuthenticationCodeInfo
from ..base_object import BaseObject


class PasswordState(BaseObject):
    """
    Represents the current state of 2-step verification
    
    Params:
        has_password (:class:`bool`)
            True, if a 2-step verification password is set
        
        password_hint (:class:`str`)
            Hint for the password; may be empty
        
        has_recovery_email_address (:class:`bool`)
            True, if a recovery email is set
        
        has_passport_data (:class:`bool`)
            True, if some Telegram Passport elements were saved
        
        recovery_email_address_code_info (:class:`EmailAddressAuthenticationCodeInfo`)
            Information about the recovery email address to which the confirmation email was sent; may be null
        
    """

    ID: str = Field("passwordState", alias="@type")
    has_password: bool
    password_hint: str
    has_recovery_email_address: bool
    has_passport_data: bool
    recovery_email_address_code_info: typing.Optional[EmailAddressAuthenticationCodeInfo] = None

    @staticmethod
    def read(q: dict) -> PasswordState:
        return PasswordState.construct(**q)
