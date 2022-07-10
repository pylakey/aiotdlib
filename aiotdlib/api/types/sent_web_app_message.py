# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SentWebAppMessage(BaseObject):
    """
    Information about the message sent by answerWebAppQuery
    
    :param inline_message_id: Identifier of the sent inline message, if known
    :type inline_message_id: :class:`str`
    
    """

    ID: str = Field("sentWebAppMessage", alias="@type")
    inline_message_id: str

    @staticmethod
    def read(q: dict) -> SentWebAppMessage:
        return SentWebAppMessage.construct(**q)
