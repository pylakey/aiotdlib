# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMenuButton(BaseObject):
    """
    Returns menu button set by the bot for the given user; for bots only

    :param user_id: Identifier of the user or 0 to get the default menu button
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getMenuButton"] = "getMenuButton"
    user_id: Int53
