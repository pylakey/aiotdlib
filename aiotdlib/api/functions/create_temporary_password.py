# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CreateTemporaryPassword(BaseObject):
    """
    Creates a new temporary password for processing payments
    
    Params:
        password (:class:`str`)
            Persistent user password
        
        valid_for (:class:`int`)
            Time during which the temporary password will be valid, in seconds; should be between 60 and 86400
        
    """

    ID: str = Field("createTemporaryPassword", alias="@type")
    password: str
    valid_for: int

    @staticmethod
    def read(q: dict) -> CreateTemporaryPassword:
        return CreateTemporaryPassword.construct(**q)
