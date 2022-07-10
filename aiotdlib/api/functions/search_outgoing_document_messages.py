# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchOutgoingDocumentMessages(BaseObject):
    """
    Searches for outgoing messages with content of the type messageDocument in all chats except secret chats. Returns the results in reverse chronological order
    
    :param query: Query to search for in document file name and message caption
    :type query: :class:`str`
    
    :param limit: The maximum number of messages to be returned; up to 100
    :type limit: :class:`int`
    
    """

    ID: str = Field("searchOutgoingDocumentMessages", alias="@type")
    query: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchOutgoingDocumentMessages:
        return SearchOutgoingDocumentMessages.construct(**q)
