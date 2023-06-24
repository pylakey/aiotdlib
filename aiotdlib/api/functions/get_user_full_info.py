# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetUserFullInfo(BaseObject):
    """
    Returns full information about a user by their identifier

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getUserFullInfo"] = "getUserFullInfo"
    user_id: Int53
