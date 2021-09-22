# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CheckRecoveryEmailAddressCode(BaseObject):
    """
    Checks the 2-step verification recovery email address verification code
    
    :param code: Verification code
    :type code: :class:`str`
    
    """

    ID: str = Field("checkRecoveryEmailAddressCode", alias="@type")
    code: str

    @staticmethod
    def read(q: dict) -> CheckRecoveryEmailAddressCode:
        return CheckRecoveryEmailAddressCode.construct(**q)
