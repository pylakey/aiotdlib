# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetBotName(BaseObject):
    """
    Returns the name of a bot in the given language. Can be called only if userTypeBot.can_be_edited == true

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param language_code: A two-letter ISO 639-1 language code or an empty string
    :type language_code: :class:`String`
    """

    ID: typing.Literal["getBotName"] = "getBotName"
    bot_user_id: Int53
    language_code: String
