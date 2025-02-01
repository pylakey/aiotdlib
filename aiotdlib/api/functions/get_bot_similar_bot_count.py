# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetBotSimilarBotCount(BaseObject):
    """
    Returns approximate number of bots similar to the given bot

    :param bot_user_id: User identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param return_local: Pass true to get the number of bots without sending network requests, or -1 if the number of bots is unknown locally
    :type return_local: :class:`Bool`
    """

    ID: typing.Literal["getBotSimilarBotCount"] = Field(
        "getBotSimilarBotCount", validation_alias="@type", alias="@type"
    )
    bot_user_id: Int53
    return_local: Bool = False
