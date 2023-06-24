# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    PassportElementType,
)


class GetPassportElement(BaseObject):
    """
    Returns one of the available Telegram Passport elements

    :param type_: Telegram Passport element type
    :type type_: :class:`PassportElementType`
    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    """

    ID: typing.Literal["getPassportElement"] = "getPassportElement"
    type_: PassportElementType = Field(..., alias="type")
    password: String
