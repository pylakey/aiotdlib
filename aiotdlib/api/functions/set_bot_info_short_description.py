# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetBotInfoShortDescription(BaseObject):
    """
    Sets the text shown on a bot's profile page and sent together with the link when users share the bot. Can be called only if userTypeBot.can_be_edited == true

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param language_code: A two-letter ISO 639-1 language code. If empty, the short description will be shown to all users for whose languages there is no dedicated description
    :type language_code: :class:`String`
    :param short_description: New bot's short description on the specified language
    :type short_description: :class:`String`
    """

    ID: typing.Literal["setBotInfoShortDescription"] = "setBotInfoShortDescription"
    bot_user_id: Int53
    language_code: String
    short_description: String
