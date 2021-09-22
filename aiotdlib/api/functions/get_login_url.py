# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetLoginUrl(BaseObject):
    """
    Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl. Use the method getLoginUrlInfo to find whether a prior user confirmation is needed. If an error is returned, then the button must be handled as an ordinary URL button
    
    :param chat_id: Chat identifier of the message with the button
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier of the message with the button
    :type message_id: :class:`int`
    
    :param button_id: Button identifier
    :type button_id: :class:`int`
    
    :param allow_write_access: True, if the user allowed the bot to send them messages
    :type allow_write_access: :class:`bool`
    
    """

    ID: str = Field("getLoginUrl", alias="@type")
    chat_id: int
    message_id: int
    button_id: int
    allow_write_access: bool

    @staticmethod
    def read(q: dict) -> GetLoginUrl:
        return GetLoginUrl.construct(**q)
