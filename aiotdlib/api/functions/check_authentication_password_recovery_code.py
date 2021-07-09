# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CheckAuthenticationPasswordRecoveryCode(BaseObject):
    """
    Checks whether a password recovery code sent to an email address is valid. Works only when the current authorization state is authorizationStateWaitPassword
    
    Params:
        recovery_code (:class:`str`)
            Recovery code to check
        
    """

    ID: str = Field("checkAuthenticationPasswordRecoveryCode", alias="@type")
    recovery_code: str

    @staticmethod
    def read(q: dict) -> CheckAuthenticationPasswordRecoveryCode:
        return CheckAuthenticationPasswordRecoveryCode.construct(**q)
