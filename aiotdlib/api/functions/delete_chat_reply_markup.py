# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteChatReplyMarkup(BaseObject):
    """
    Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a replyMarkupForceReply reply markup has been used. An updateChatReplyMarkup update will be sent if the reply markup is changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: The message identifier of the used keyboard
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["deleteChatReplyMarkup"] = "deleteChatReplyMarkup"
    chat_id: Int53
    message_id: Int53
