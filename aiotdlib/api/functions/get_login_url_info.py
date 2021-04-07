# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetLoginUrlInfo(BaseObject):
    """
    Returns information about a button of type inlineKeyboardButtonTypeLoginUrl. The method needs to be called when the user presses the button
    
    Params:
        chat_id (:class:`int`)
            Chat identifier of the message with the button
        
        message_id (:class:`int`)
            Message identifier of the message with the button
        
        button_id (:class:`int`)
            Button identifier
        
    """

    ID: str = Field("getLoginUrlInfo", alias="@type")
    chat_id: int
    message_id: int
    button_id: int

    @staticmethod
    def read(q: dict) -> GetLoginUrlInfo:
        return GetLoginUrlInfo.construct(**q)
