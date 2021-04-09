# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .message_reply_info import MessageReplyInfo
from ..base_object import BaseObject


class MessageInteractionInfo(BaseObject):
    """
    Contains information about interactions with a message
    
    Params:
        view_count (:class:`int`)
            Number of times the message was viewed
        
        forward_count (:class:`int`)
            Number of times the message was forwarded
        
        reply_info (:class:`MessageReplyInfo`)
            Contains information about direct or indirect replies to the message; may be null. Currently, available only in channels with a discussion supergroup and discussion supergroups for messages, which are not replies itself
        
    """

    ID: str = Field("messageInteractionInfo", alias="@type")
    view_count: int
    forward_count: int
    reply_info: typing.Optional[MessageReplyInfo] = None

    @staticmethod
    def read(q: dict) -> MessageInteractionInfo:
        return MessageInteractionInfo.construct(**q)
