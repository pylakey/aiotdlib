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
    MessageSender,
)


class SetVideoChatDefaultParticipant(BaseObject):
    """
    Changes default participant identifier, on whose behalf a video chat in the chat will be joined

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param default_participant_id: Default group call participant identifier to join the video chats
    :type default_participant_id: :class:`MessageSender`
    """

    ID: typing.Literal["setVideoChatDefaultParticipant"] = "setVideoChatDefaultParticipant"
    chat_id: Int53
    default_participant_id: MessageSender
