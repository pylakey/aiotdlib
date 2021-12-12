# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CheckAuthenticationCode(BaseObject):
    """
    Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode
    
    :param code: Authentication code to check
    :type code: :class:`str`
    
    """

    ID: str = Field("checkAuthenticationCode", alias="@type")
    code: str

    @staticmethod
    def read(q: dict) -> CheckAuthenticationCode:
        return CheckAuthenticationCode.construct(**q)
