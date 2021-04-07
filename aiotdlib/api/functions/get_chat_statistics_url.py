# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatStatisticsUrl(BaseObject):
    """
    Returns an HTTP URL with the chat statistics. Currently this method of getting the statistics are disabled and can be deleted in the future
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        parameters (:class:`str`)
            Parameters from "tg://statsrefresh?params=******" link
        
        is_dark (:class:`bool`)
            Pass true if a URL with the dark theme must be returned
        
    """

    ID: str = Field("getChatStatisticsUrl", alias="@type")
    chat_id: int
    parameters: str
    is_dark: bool

    @staticmethod
    def read(q: dict) -> GetChatStatisticsUrl:
        return GetChatStatisticsUrl.construct(**q)
