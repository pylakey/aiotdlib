# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RecoverAuthenticationPassword(BaseObject):
    """
    Recovers the password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
    
    Params:
        recovery_code (:class:`str`)
            Recovery code to check
        
        new_password (:class:`str`)
            New password of the user; may be empty to remove the password
        
        new_hint (:class:`str`)
            New password hint; may be empty
        
    """

    ID: str = Field("recoverAuthenticationPassword", alias="@type")
    recovery_code: str
    new_password: str
    new_hint: str

    @staticmethod
    def read(q: dict) -> RecoverAuthenticationPassword:
        return RecoverAuthenticationPassword.construct(**q)
