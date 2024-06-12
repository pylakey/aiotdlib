# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RecognizeSpeech(BaseObject):
    """
    Recognizes speech in a video note or a voice note message. The message must be successfully sent, must not be scheduled, and must be from a non-secret chat

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["recognizeSpeech"] = Field("recognizeSpeech", validation_alias="@type", alias="@type")
    chat_id: Int53
    message_id: Int53
