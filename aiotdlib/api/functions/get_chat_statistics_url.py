# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetChatStatisticsUrl(BaseObject):
    """
    Returns an HTTP URL with the chat statistics. Currently this method of getting the statistics are disabled and can be deleted in the future
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param parameters: Parameters for the request
    :type parameters: :class:`str`
    
    :param is_dark: Pass true if a URL with the dark theme must be returned
    :type is_dark: :class:`bool`
    
    """

    ID: str = Field("getChatStatisticsUrl", alias="@type")
    chat_id: int
    parameters: str
    is_dark: bool

    @staticmethod
    def read(q: dict) -> GetChatStatisticsUrl:
        return GetChatStatisticsUrl.construct(**q)
