# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class RecoverPassword(BaseObject):
    """
    Recovers the 2-step verification password using a recovery code sent to an email address that was previously set up
    
    :param recovery_code: Recovery code to check
    :type recovery_code: :class:`str`
    
    :param new_password: New password of the user; may be empty to remove the password
    :type new_password: :class:`str`
    
    :param new_hint: New password hint; may be empty
    :type new_hint: :class:`str`
    
    """

    ID: str = Field("recoverPassword", alias="@type")
    recovery_code: str
    new_password: str
    new_hint: str

    @staticmethod
    def read(q: dict) -> RecoverPassword:
        return RecoverPassword.construct(**q)
