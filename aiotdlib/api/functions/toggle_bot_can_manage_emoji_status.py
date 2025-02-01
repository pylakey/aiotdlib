# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleBotCanManageEmojiStatus(BaseObject):
    """
    Toggles whether the bot can manage emoji status of the current user

    :param bot_user_id: User identifier of the bot
    :type bot_user_id: :class:`Int53`
    :param can_manage_emoji_status: Pass true if the bot is allowed to change emoji status of the user; pass false otherwise
    :type can_manage_emoji_status: :class:`Bool`
    """

    ID: typing.Literal["toggleBotCanManageEmojiStatus"] = Field(
        "toggleBotCanManageEmojiStatus", validation_alias="@type", alias="@type"
    )
    bot_user_id: Int53
    can_manage_emoji_status: Bool = False
