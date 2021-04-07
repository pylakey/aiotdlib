# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class BlockMessageSenderFromReplies(BaseObject):
    """
    Blocks an original sender of a message in the Replies chat
    
    Params:
        message_id (:class:`int`)
            The identifier of an incoming message in the Replies chat
        
        delete_message (:class:`bool`)
            Pass true if the message must be deleted
        
        delete_all_messages (:class:`bool`)
            Pass true if all messages from the same sender must be deleted
        
        report_spam (:class:`bool`)
            Pass true if the sender must be reported to the Telegram moderators
        
    """

    ID: str = Field("blockMessageSenderFromReplies", alias="@type")
    message_id: int
    delete_message: bool
    delete_all_messages: bool
    report_spam: bool

    @staticmethod
    def read(q: dict) -> BlockMessageSenderFromReplies:
        return BlockMessageSenderFromReplies.construct(**q)
