# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchChatsOnServer(BaseObject):
    """
    Searches for the specified query in the title and username of already known chats via request to the server. Returns chats in the order seen in the main chat list

    :param query: Query to search for
    :type query: :class:`String`
    :param limit: The maximum number of chats to be returned
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchChatsOnServer"] = "searchChatsOnServer"
    query: String
    limit: Int32
