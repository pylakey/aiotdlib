# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReaddQuickReplyShortcutMessages(BaseObject):
    """
    Readds quick reply messages which failed to add. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed. If a message is readded, the corresponding failed to send message is deleted. Returns the sent messages in the same order as the message identifiers passed in message_ids. If a message can't be readded, null will be returned instead of the message

    :param shortcut_name: Name of the target shortcut
    :type shortcut_name: :class:`String`
    :param message_ids: Identifiers of the quick reply messages to readd. Message identifiers must be in a strictly increasing order
    :type message_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["readdQuickReplyShortcutMessages"] = Field(
        "readdQuickReplyShortcutMessages", validation_alias="@type", alias="@type"
    )
    shortcut_name: String
    message_ids: Vector[Int53]
