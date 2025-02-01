# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetBotSimilarBots(BaseObject):
    """
    Returns a list of bots similar to the given bot

    :param bot_user_id: User identifier of the target bot
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["getBotSimilarBots"] = Field("getBotSimilarBots", validation_alias="@type", alias="@type")
    bot_user_id: Int53
