# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetBotName(BaseObject):
    """
    Sets the name of a bot. Can be called only if userTypeBot.can_be_edited == true

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param language_code: A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose languages there is no dedicated name
    :type language_code: :class:`String`
    :param name: New bot's name on the specified language; 0-64 characters; must be non-empty if language code is empty
    :type name: :class:`String`
    """

    ID: typing.Literal["setBotName"] = "setBotName"
    bot_user_id: Int53
    language_code: String
    name: String = Field("", max_length=64)
