# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_sender import MessageSender
from ..base_object import BaseObject


class UnreadReaction(BaseObject):
    """
    Contains information about an unread reaction to a message
    
    :param reaction: Text representation of the reaction
    :type reaction: :class:`str`
    
    :param sender_id: Identifier of the sender, added the reaction
    :type sender_id: :class:`MessageSender`
    
    :param is_big: True, if the reaction was added with a big animation
    :type is_big: :class:`bool`
    
    """

    ID: str = Field("unreadReaction", alias="@type")
    reaction: str
    sender_id: MessageSender
    is_big: bool

    @staticmethod
    def read(q: dict) -> UnreadReaction:
        return UnreadReaction.construct(**q)
