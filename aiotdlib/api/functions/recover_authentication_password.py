# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class RecoverAuthenticationPassword(BaseObject):
    """
    Recovers the password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
    
    :param recovery_code: Recovery code to check
    :type recovery_code: :class:`str`
    
    :param new_password: New password of the user; may be empty to remove the password
    :type new_password: :class:`str`
    
    :param new_hint: New password hint; may be empty
    :type new_hint: :class:`str`
    
    """

    ID: str = Field("recoverAuthenticationPassword", alias="@type")
    recovery_code: str
    new_password: str
    new_hint: str

    @staticmethod
    def read(q: dict) -> RecoverAuthenticationPassword:
        return RecoverAuthenticationPassword.construct(**q)
