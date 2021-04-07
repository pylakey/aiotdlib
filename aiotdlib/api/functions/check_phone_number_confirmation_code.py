# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CheckPhoneNumberConfirmationCode(BaseObject):
    """
    Checks phone number confirmation code
    
    Params:
        code (:class:`str`)
            The phone number confirmation code
        
    """

    ID: str = Field("checkPhoneNumberConfirmationCode", alias="@type")
    code: str

    @staticmethod
    def read(q: dict) -> CheckPhoneNumberConfirmationCode:
        return CheckPhoneNumberConfirmationCode.construct(**q)
