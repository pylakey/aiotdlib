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
    
    :param has_password: True, if a 2-step verification password is set
    :type has_password: :class:`bool`
    
    :param password_hint: Hint for the password; may be empty
    :type password_hint: :class:`str`
    
    :param has_recovery_email_address: True, if a recovery email is set
    :type has_recovery_email_address: :class:`bool`
    
    :param has_passport_data: True, if some Telegram Passport elements were saved
    :type has_passport_data: :class:`bool`
    
    :param recovery_email_address_code_info: Information about the recovery email address to which the confirmation email was sent; may be null, defaults to None
    :type recovery_email_address_code_info: :class:`EmailAddressAuthenticationCodeInfo`, optional
    
    :param pending_reset_date: If not 0, point in time (Unix timestamp) after which the password can be reset immediately using resetPassword
    :type pending_reset_date: :class:`int`
    
    """

    ID: str = Field("passwordState", alias="@type")
    has_password: bool
    password_hint: str
    has_recovery_email_address: bool
    has_passport_data: bool
    recovery_email_address_code_info: typing.Optional[EmailAddressAuthenticationCodeInfo] = None
    pending_reset_date: int

    @staticmethod
    def read(q: dict) -> PasswordState:
        return PasswordState.construct(**q)
