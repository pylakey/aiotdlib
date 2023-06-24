# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchOutgoingDocumentMessages(BaseObject):
    """
    Searches for outgoing messages with content of the type messageDocument in all chats except secret chats. Returns the results in reverse chronological order

    :param query: Query to search for in document file name and message caption
    :type query: :class:`String`
    :param limit: The maximum number of messages to be returned; up to 100
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchOutgoingDocumentMessages"] = "searchOutgoingDocumentMessages"
    query: String
    limit: Int32
