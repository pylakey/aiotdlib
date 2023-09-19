# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    Location,
)


class GetInlineQueryResults(BaseObject):
    """
    Sends an inline query to a bot and returns its results. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param chat_id: Identifier of the chat where the query was sent
    :type chat_id: :class:`Int53`
    :param query: Text of the query
    :type query: :class:`String`
    :param offset: Offset of the first entry to return; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param user_location: Location of the user; pass null if unknown or the bot doesn't need user's location, defaults to None
    :type user_location: :class:`Location`, optional
    """

    ID: typing.Literal["getInlineQueryResults"] = "getInlineQueryResults"
    bot_user_id: Int53
    chat_id: Int53
    query: String
    offset: String
    user_location: typing.Optional[Location] = None
