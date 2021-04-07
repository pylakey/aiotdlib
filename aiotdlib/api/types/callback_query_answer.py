# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CallbackQueryAnswer(BaseObject):
    """
    Contains a bot's answer to a callback query
    
    Params:
        text (:class:`str`)
            Text of the answer
        
        show_alert (:class:`bool`)
            True, if an alert should be shown to the user instead of a toast notification
        
        url (:class:`str`)
            URL to be opened
        
    """

    ID: str = Field("callbackQueryAnswer", alias="@type")
    text: str
    show_alert: bool
    url: str

    @staticmethod
    def read(q: dict) -> CallbackQueryAnswer:
        return CallbackQueryAnswer.construct(**q)
