# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RequestAuthenticationPasswordRecovery(BaseObject):
    """
    Requests to send a password recovery code to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
    
    """

    ID: str = Field("requestAuthenticationPasswordRecovery", alias="@type")

    @staticmethod
    def read(q: dict) -> RequestAuthenticationPasswordRecovery:
        return RequestAuthenticationPasswordRecovery.construct(**q)
