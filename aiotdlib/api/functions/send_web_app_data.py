# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SendWebAppData(BaseObject):
    """
    Sends data received from a keyboardButtonTypeWebApp Web App to a bot
    
    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`int`
    
    :param button_text: Text of the keyboardButtonTypeWebApp button, which opened the Web App
    :type button_text: :class:`str`
    
    :param data: Received data
    :type data: :class:`str`
    
    """

    ID: str = Field("sendWebAppData", alias="@type")
    bot_user_id: int
    button_text: str
    data: str

    @staticmethod
    def read(q: dict) -> SendWebAppData:
        return SendWebAppData.construct(**q)
