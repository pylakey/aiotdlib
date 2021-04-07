# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetLoginUrl(BaseObject):
    """
    Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl. Use the method getLoginUrlInfo to find whether a prior user confirmation is needed. If an error is returned, then the button must be handled as an ordinary URL button
    
    Params:
        chat_id (:class:`int`)
            Chat identifier of the message with the button
        
        message_id (:class:`int`)
            Message identifier of the message with the button
        
        button_id (:class:`int`)
            Button identifier
        
        allow_write_access (:class:`bool`)
            True, if the user allowed the bot to send them messages
        
    """

    ID: str = Field("getLoginUrl", alias="@type")
    chat_id: int
    message_id: int
    button_id: int
    allow_write_access: bool

    @staticmethod
    def read(q: dict) -> GetLoginUrl:
        return GetLoginUrl.construct(**q)
