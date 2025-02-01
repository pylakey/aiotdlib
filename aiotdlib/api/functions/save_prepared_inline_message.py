# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    InputInlineQueryResult,
    TargetChatTypes,
)


class SavePreparedInlineMessage(BaseObject):
    """
    Saves an inline message to be sent by the given user; for bots only

    :param user_id: Identifier of the user
    :type user_id: :class:`Int53`
    :param result: The description of the message
    :type result: :class:`InputInlineQueryResult`
    :param chat_types: Types of the chats to which the message can be sent
    :type chat_types: :class:`TargetChatTypes`
    """

    ID: typing.Literal["savePreparedInlineMessage"] = Field(
        "savePreparedInlineMessage", validation_alias="@type", alias="@type"
    )
    user_id: Int53
    result: InputInlineQueryResult
    chat_types: TargetChatTypes
