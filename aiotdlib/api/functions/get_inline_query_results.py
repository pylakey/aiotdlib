# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import Location


class GetInlineQueryResults(BaseObject):
    """
    Sends an inline query to a bot and returns its results. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
    
    Params:
        bot_user_id (:class:`int`)
            The identifier of the target bot
        
        chat_id (:class:`int`)
            Identifier of the chat where the query was sent
        
        user_location (:class:`Location`)
            Location of the user, only if needed
        
        query (:class:`str`)
            Text of the query
        
        offset (:class:`str`)
            Offset of the first entry to return
        
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
