# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CallbackQueryAnswer(BaseObject):
    """
    Contains a bot's answer to a callback query
    
    :param text: Text of the answer
    :type text: :class:`str`
    
    :param show_alert: True, if an alert should be shown to the user instead of a toast notification
    :type show_alert: :class:`bool`
    
    :param url: URL to be opened
    :type url: :class:`str`
    
    """

    ID: str = Field("callbackQueryAnswer", alias="@type")
    text: str
    show_alert: bool
    url: str

    @staticmethod
    def read(q: dict) -> CallbackQueryAnswer:
        return CallbackQueryAnswer.construct(**q)
