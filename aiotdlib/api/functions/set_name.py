# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetName(BaseObject):
    """
    Changes the first and last name of the current user

    :param first_name: The new value of the first name for the current user; 1-64 characters
    :type first_name: :class:`String`
    :param last_name: The new value of the optional last name for the current user; 0-64 characters
    :type last_name: :class:`String`
    """

    ID: typing.Literal["setName"] = "setName"
    first_name: String = Field(..., min_length=1, max_length=64)
    last_name: String = Field("", max_length=64)
