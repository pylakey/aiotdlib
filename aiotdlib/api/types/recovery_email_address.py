# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RecoveryEmailAddress(BaseObject):
    """
    Contains information about the current recovery email address
    
    Params:
        recovery_email_address (:class:`str`)
            Recovery email address
        
    """

    ID: str = Field("recoveryEmailAddress", alias="@type")
    recovery_email_address: str

    @staticmethod
    def read(q: dict) -> RecoveryEmailAddress:
        return RecoveryEmailAddress.construct(**q)
