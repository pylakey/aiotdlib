# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class BlockMessageSenderFromReplies(BaseObject):
    """
    Blocks an original sender of a message in the Replies chat
    
    :param message_id: The identifier of an incoming message in the Replies chat
    :type message_id: :class:`int`
    
    :param delete_message: Pass true if the message must be deleted
    :type delete_message: :class:`bool`
    
    :param delete_all_messages: Pass true if all messages from the same sender must be deleted
    :type delete_all_messages: :class:`bool`
    
    :param report_spam: Pass true if the sender must be reported to the Telegram moderators
    :type report_spam: :class:`bool`
    
    """

    ID: str = Field("blockMessageSenderFromReplies", alias="@type")
    message_id: int
    delete_message: bool
    delete_all_messages: bool
    report_spam: bool

    @staticmethod
    def read(q: dict) -> BlockMessageSenderFromReplies:
        return BlockMessageSenderFromReplies.construct(**q)
