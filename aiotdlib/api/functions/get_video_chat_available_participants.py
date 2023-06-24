# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetVideoChatAvailableParticipants(BaseObject):
    """
    Returns list of participant identifiers, on whose behalf a video chat in the chat can be joined

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getVideoChatAvailableParticipants"] = "getVideoChatAvailableParticipants"
    chat_id: Int53
