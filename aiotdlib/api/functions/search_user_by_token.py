# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchUserByToken(BaseObject):
    """
    Searches a user by a token from the user's link

    :param token: Token to search for
    :type token: :class:`String`
    """

    ID: typing.Literal["searchUserByToken"] = Field("searchUserByToken", validation_alias="@type", alias="@type")
    token: String
