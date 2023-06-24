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
    BotMenuButton,
)


class SetMenuButton(BaseObject):
    """
    Sets menu button for the given user or for all users; for bots only

    :param user_id: Identifier of the user or 0 to set menu button for all users
    :type user_id: :class:`Int53`
    :param menu_button: New menu button
    :type menu_button: :class:`BotMenuButton`
    """

    ID: typing.Literal["setMenuButton"] = "setMenuButton"
    user_id: Int53
    menu_button: BotMenuButton
