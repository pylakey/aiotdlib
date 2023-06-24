# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class BlockMessageSenderFromReplies(BaseObject):
    """
    Blocks an original sender of a message in the Replies chat

    :param message_id: The identifier of an incoming message in the Replies chat
    :type message_id: :class:`Int53`
    :param delete_message: Pass true to delete the message
    :type delete_message: :class:`Bool`
    :param delete_all_messages: Pass true to delete all messages from the same sender
    :type delete_all_messages: :class:`Bool`
    :param report_spam: Pass true to report the sender to the Telegram moderators
    :type report_spam: :class:`Bool`
    """

    ID: typing.Literal["blockMessageSenderFromReplies"] = "blockMessageSenderFromReplies"
    message_id: Int53
    delete_message: Bool = False
    delete_all_messages: Bool = False
    report_spam: Bool = False
