# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetUserSupportInfo(BaseObject):
    """
    Returns support information for the given user; for Telegram support only

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getUserSupportInfo"] = "getUserSupportInfo"
    user_id: Int53
