# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMessageLocally(BaseObject):
    """
    Returns information about a message, if it is available without sending network request. Returns a 404 error if message isn't available locally. This is an offline method

    :param chat_id: Identifier of the chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message to get
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["getMessageLocally"] = Field("getMessageLocally", validation_alias="@type", alias="@type")
    chat_id: Int53
    message_id: Int53
