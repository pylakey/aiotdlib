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
    Birthdate,
)


class SetBirthdate(BaseObject):
    """
    Changes the birthdate of the current user

    :param birthdate: The new value of the current user's birthdate; pass null to remove the birthdate, defaults to None
    :type birthdate: :class:`Birthdate`, optional
    """

    ID: typing.Literal["setBirthdate"] = Field("setBirthdate", validation_alias="@type", alias="@type")
    birthdate: typing.Optional[Birthdate] = None
