# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetBotInfoDescription(BaseObject):
    """
    Sets the text shown in the chat with a bot if the chat is empty. Can be called only if userTypeBot.can_be_edited == true

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param language_code: A two-letter ISO 639-1 language code. If empty, the description will be shown to all users for whose languages there is no dedicated description
    :type language_code: :class:`String`
    :param description: New bot's description on the specified language
    :type description: :class:`String`
    """

    ID: typing.Literal["setBotInfoDescription"] = "setBotInfoDescription"
    bot_user_id: Int53
    language_code: String
    description: String
