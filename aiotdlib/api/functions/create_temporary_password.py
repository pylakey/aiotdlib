# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CreateTemporaryPassword(BaseObject):
    """
    Creates a new temporary password for processing payments
    
    :param password: Persistent user password
    :type password: :class:`str`
    
    :param valid_for: Time during which the temporary password will be valid, in seconds; should be between 60 and 86400
    :type valid_for: :class:`int`
    
    """

    ID: str = Field("createTemporaryPassword", alias="@type")
    password: str
    valid_for: int

    @staticmethod
    def read(q: dict) -> CreateTemporaryPassword:
        return CreateTemporaryPassword.construct(**q)
