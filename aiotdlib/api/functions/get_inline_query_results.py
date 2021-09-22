# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import Location
from ..base_object import BaseObject


class GetInlineQueryResults(BaseObject):
    """
    Sends an inline query to a bot and returns its results. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
    
    :param bot_user_id: The identifier of the target bot
    :type bot_user_id: :class:`int`
    
    :param chat_id: Identifier of the chat where the query was sent
    :type chat_id: :class:`int`
    
    :param user_location: Location of the user, only if needed
    :type user_location: :class:`Location`
    
    :param query: Text of the query
    :type query: :class:`str`
    
    :param offset: Offset of the first entry to return
    :type offset: :class:`str`
    
    """

    ID: str = Field("getInlineQueryResults", alias="@type")
    bot_user_id: int
    chat_id: int
    user_location: Location
    query: str
    offset: str

    @staticmethod
    def read(q: dict) -> GetInlineQueryResults:
        return GetInlineQueryResults.construct(**q)
