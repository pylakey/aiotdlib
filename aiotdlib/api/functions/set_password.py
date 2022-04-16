# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetPassword(BaseObject):
    """
    Changes the password for the current user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed
    
    :param old_password: Previous password of the user
    :type old_password: :class:`str`
    
    :param new_password: New password of the user; may be empty to remove the password
    :type new_password: :class:`str`
    
    :param new_hint: New password hint; may be empty
    :type new_hint: :class:`str`
    
    :param set_recovery_email_address: Pass true to change also the recovery email address
    :type set_recovery_email_address: :class:`bool`
    
    :param new_recovery_email_address: New recovery email address; may be empty
    :type new_recovery_email_address: :class:`str`
    
    """

    ID: str = Field("setPassword", alias="@type")
    old_password: str
    new_password: str
    new_hint: str
    set_recovery_email_address: bool
    new_recovery_email_address: str

    @staticmethod
    def read(q: dict) -> SetPassword:
        return SetPassword.construct(**q)
