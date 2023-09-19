# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AllowBotToSendMessages(BaseObject):
    """
    Allows the specified bot to send messages to the user

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["allowBotToSendMessages"] = "allowBotToSendMessages"
    bot_user_id: Int53
