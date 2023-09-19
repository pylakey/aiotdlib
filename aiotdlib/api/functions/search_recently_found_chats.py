# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchRecentlyFoundChats(BaseObject):
    """
    Searches for the specified query in the title and username of up to 50 recently found chats; this is an offline request

    :param query: Query to search for
    :type query: :class:`String`
    :param limit: The maximum number of chats to be returned
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchRecentlyFoundChats"] = "searchRecentlyFoundChats"
    query: String
    limit: Int32
