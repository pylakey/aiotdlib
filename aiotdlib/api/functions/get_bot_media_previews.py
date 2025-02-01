# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetBotMediaPreviews(BaseObject):
    """
    Returns the list of media previews of a bot

    :param bot_user_id: Identifier of the target bot. The bot must have the main Web App
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["getBotMediaPreviews"] = Field("getBotMediaPreviews", validation_alias="@type", alias="@type")
    bot_user_id: Int53
