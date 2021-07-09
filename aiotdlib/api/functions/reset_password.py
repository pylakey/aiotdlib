# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ResetPassword(BaseObject):
    """
    Removes 2-step verification password without previous password and access to recovery email address. The password can't be reset immediately and the request needs to be repeated after the specified time
    
    """

    ID: str = Field("resetPassword", alias="@type")

    @staticmethod
    def read(q: dict) -> ResetPassword:
        return ResetPassword.construct(**q)
