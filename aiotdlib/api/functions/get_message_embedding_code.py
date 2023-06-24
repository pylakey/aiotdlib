# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMessageEmbeddingCode(BaseObject):
    """
    Returns an HTML code for embedding the message. Available only for messages in supergroups and channels with a username

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param for_album: Pass true to return an HTML code for embedding of the whole media album
    :type for_album: :class:`Bool`
    """

    ID: typing.Literal["getMessageEmbeddingCode"] = "getMessageEmbeddingCode"
    chat_id: Int53
    message_id: Int53
    for_album: Bool = False
