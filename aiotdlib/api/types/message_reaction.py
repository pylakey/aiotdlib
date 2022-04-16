# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_sender import MessageSender
from ..base_object import BaseObject


class MessageReaction(BaseObject):
    """
    Contains information about a reaction to a message
    
    :param reaction: Text representation of the reaction
    :type reaction: :class:`str`
    
    :param total_count: Number of times the reaction was added
    :type total_count: :class:`int`
    
    :param is_chosen: True, if the reaction is chosen by the current user
    :type is_chosen: :class:`bool`
    
    :param recent_sender_ids: Identifiers of at most 3 recent message senders, added the reaction; available in private, basic group and supergroup chats
    :type recent_sender_ids: :class:`list[MessageSender]`
    
    """

    ID: str = Field("messageReaction", alias="@type")
    reaction: str
    total_count: int
    is_chosen: bool
    recent_sender_ids: list[MessageSender]

    @staticmethod
    def read(q: dict) -> MessageReaction:
        return MessageReaction.construct(**q)
