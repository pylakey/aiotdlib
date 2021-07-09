# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ResendAuthenticationCode(BaseObject):
    """
    Re-sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitCode, the next_code_type of the result is not null and the server-specified timeout has passed
    
    """

    ID: str = Field("resendAuthenticationCode", alias="@type")

    @staticmethod
    def read(q: dict) -> ResendAuthenticationCode:
        return ResendAuthenticationCode.construct(**q)
