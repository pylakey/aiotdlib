# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Error(BaseObject):
    """
    An object of this type can be returned on every function call, in case of an error
    
    :param code: Error code; subject to future changes. If the error code is 406, the error message must not be processed in any way and must not be displayed to the user
    :type code: :class:`int`
    
    :param message: Error message; subject to future changes
    :type message: :class:`str`
    
    """

    ID: str = Field("error", alias="@type")
    code: int
    message: str

    @staticmethod
    def read(q: dict) -> Error:
        return Error.construct(**q)
