# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RecoverPassword(BaseObject):
    """
    Recovers the password using a recovery code sent to an email address that was previously set up
    
    Params:
        recovery_code (:class:`str`)
            Recovery code to check
        
    """

    ID: str = Field("recoverPassword", alias="@type")
    recovery_code: str

    @staticmethod
    def read(q: dict) -> RecoverPassword:
        return RecoverPassword.construct(**q)
