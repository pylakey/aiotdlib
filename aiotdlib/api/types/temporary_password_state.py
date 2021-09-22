# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class TemporaryPasswordState(BaseObject):
    """
    Returns information about the availability of a temporary password, which can be used for payments
    
    :param has_password: True, if a temporary password is available
    :type has_password: :class:`bool`
    
    :param valid_for: Time left before the temporary password expires, in seconds
    :type valid_for: :class:`int`
    
    """

    ID: str = Field("temporaryPasswordState", alias="@type")
    has_password: bool
    valid_for: int

    @staticmethod
    def read(q: dict) -> TemporaryPasswordState:
        return TemporaryPasswordState.construct(**q)
