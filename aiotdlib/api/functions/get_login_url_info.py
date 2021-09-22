# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetLoginUrlInfo(BaseObject):
    """
    Returns information about a button of type inlineKeyboardButtonTypeLoginUrl. The method needs to be called when the user presses the button
    
    :param chat_id: Chat identifier of the message with the button
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier of the message with the button
    :type message_id: :class:`int`
    
    :param button_id: Button identifier
    :type button_id: :class:`int`
    
    """

    ID: str = Field("getLoginUrlInfo", alias="@type")
    chat_id: int
    message_id: int
    button_id: int

    @staticmethod
    def read(q: dict) -> GetLoginUrlInfo:
        return GetLoginUrlInfo.construct(**q)
