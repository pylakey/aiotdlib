# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CheckAuthenticationPassword(BaseObject):
    """
    Checks the authentication password for correctness. Works only when the current authorization state is authorizationStateWaitPassword
    
    Params:
        password (:class:`str`)
            The password to check
        
    """

    ID: str = Field("checkAuthenticationPassword", alias="@type")
    password: str

    @staticmethod
    def read(q: dict) -> CheckAuthenticationPassword:
        return CheckAuthenticationPassword.construct(**q)
