# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteBusinessConnectedBot(BaseObject):
    """
    Deletes the business bot that is connected to the current user account

    :param bot_user_id: Unique user identifier for the bot
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["deleteBusinessConnectedBot"] = Field(
        "deleteBusinessConnectedBot", validation_alias="@type", alias="@type"
    )
    bot_user_id: Int53
