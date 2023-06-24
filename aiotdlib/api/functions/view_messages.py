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
    MessageSource,
)


class ViewMessages(BaseObject):
    """
    Informs TDLib that messages are being viewed by the user. Sponsored messages must be marked as viewed only when the entire text of the message is shown on the screen (excluding the button). Many useful activities depend on whether the messages are currently being viewed or not (e.g., marking messages as read, incrementing a view counter, updating a view counter, removing deleted messages in supergroups and channels)

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_ids: The identifiers of the messages being viewed
    :type message_ids: :class:`Vector[Int53]`
    :param force_read: Pass true to mark as read the specified messages even the chat is closed
    :type force_read: :class:`Bool`
    :param source: Source of the message view; pass null to guess the source based on chat open state, defaults to None
    :type source: :class:`MessageSource`, optional
    """

    ID: typing.Literal["viewMessages"] = "viewMessages"
    chat_id: Int53
    message_ids: Vector[Int53]
    force_read: Bool = False
    source: typing.Optional[MessageSource] = None
