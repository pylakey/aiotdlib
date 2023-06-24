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


class DeletePassportElement(BaseObject):
    """
    Deletes a Telegram Passport element

    :param type_: Element type
    :type type_: :class:`PassportElementType`
    """

    ID: typing.Literal["deletePassportElement"] = "deletePassportElement"
    type_: PassportElementType = Field(..., alias="type")
