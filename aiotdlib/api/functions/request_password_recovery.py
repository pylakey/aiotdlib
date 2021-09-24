# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RequestPasswordRecovery(BaseObject):
    """
    Requests to send a 2-step verification password recovery code to an email address that was previously set up
    
    """

    ID: str = Field("requestPasswordRecovery", alias="@type")

    @staticmethod
    def read(q: dict) -> RequestPasswordRecovery:
        return RequestPasswordRecovery.construct(**q)
