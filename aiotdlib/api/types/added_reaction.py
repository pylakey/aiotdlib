# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_sender import MessageSender
from ..base_object import BaseObject


class AddedReaction(BaseObject):
    """
    Represents a reaction applied to a message
    
    :param reaction: Text representation of the reaction
    :type reaction: :class:`str`
    
    :param sender_id: Identifier of the chat member, applied the reaction
    :type sender_id: :class:`MessageSender`
    
    """

    ID: str = Field("addedReaction", alias="@type")
    reaction: str
    sender_id: MessageSender

    @staticmethod
    def read(q: dict) -> AddedReaction:
        return AddedReaction.construct(**q)
