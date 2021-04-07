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
    Changes the password for the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed
    
    Params:
        old_password (:class:`str`)
            Previous password of the user
        
        new_password (:class:`str`)
            New password of the user; may be empty to remove the password
        
        new_hint (:class:`str`)
            New password hint; may be empty
        
        set_recovery_email_address (:class:`bool`)
            Pass true if the recovery email address should be changed
        
        new_recovery_email_address (:class:`str`)
            New recovery email address; may be empty
        
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
