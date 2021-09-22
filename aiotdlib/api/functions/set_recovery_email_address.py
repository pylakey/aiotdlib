# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetRecoveryEmailAddress(BaseObject):
    """
    Changes the 2-step verification recovery email address of the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed. If new_recovery_email_address is the same as the email address that is currently set up, this call succeeds immediately and aborts all other requests waiting for an email confirmation
    
    :param password: Password of the current user
    :type password: :class:`str`
    
    :param new_recovery_email_address: New recovery email address
    :type new_recovery_email_address: :class:`str`
    
    """

    ID: str = Field("setRecoveryEmailAddress", alias="@type")
    password: str
    new_recovery_email_address: str

    @staticmethod
    def read(q: dict) -> SetRecoveryEmailAddress:
        return SetRecoveryEmailAddress.construct(**q)
