# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetMessageReaction(BaseObject):
    """
    Changes chosen reaction for a message
    
    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param reaction: Text representation of the new chosen reaction. Can be an empty string or the currently chosen non-big reaction to remove the reaction
    :type reaction: :class:`str`
    
    :param is_big: Pass true if the reaction is added with a big animation
    :type is_big: :class:`bool`
    
    """

    ID: str = Field("setMessageReaction", alias="@type")
    chat_id: int
    message_id: int
    reaction: str
    is_big: bool

    @staticmethod
    def read(q: dict) -> SetMessageReaction:
        return SetMessageReaction.construct(**q)
