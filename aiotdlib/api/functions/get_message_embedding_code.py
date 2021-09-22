# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetMessageEmbeddingCode(BaseObject):
    """
    Returns an HTML code for embedding the message. Available only for messages in supergroups and channels with a username
    
    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param for_album: Pass true to return an HTML code for embedding of the whole media album
    :type for_album: :class:`bool`
    
    """

    ID: str = Field("getMessageEmbeddingCode", alias="@type")
    chat_id: int
    message_id: int
    for_album: bool

    @staticmethod
    def read(q: dict) -> GetMessageEmbeddingCode:
        return GetMessageEmbeddingCode.construct(**q)
