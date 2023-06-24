# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchPublicChats(BaseObject):
    """
    Searches public chats by looking for specified query in their username and title. Currently, only private chats, supergroups and channels can be public. Returns a meaningful number of results. Excludes private chats with contacts and chats from the chat list from the results

    :param query: Query to search for
    :type query: :class:`String`
    """

    ID: typing.Literal["searchPublicChats"] = "searchPublicChats"
    query: String
