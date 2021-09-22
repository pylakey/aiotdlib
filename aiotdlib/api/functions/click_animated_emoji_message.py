# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ClickAnimatedEmojiMessage(BaseObject):
    """
    Informs TDLib that a message with an animated emoji was clicked by the user. Returns a big animated sticker to be played or a 404 error if usual animation needs to be played
    
    :param chat_id: Chat identifier of the message
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the clicked message
    :type message_id: :class:`int`
    
    """

    ID: str = Field("clickAnimatedEmojiMessage", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> ClickAnimatedEmojiMessage:
        return ClickAnimatedEmojiMessage.construct(**q)
