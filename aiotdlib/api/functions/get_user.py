# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetUser(BaseObject):
    """
    Returns information about a user by their identifier. This is an offline method if the current user is not a bot

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getUser"] = Field("getUser", validation_alias="@type", alias="@type")
    user_id: Int53
