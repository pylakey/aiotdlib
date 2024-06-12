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
    Returns the list of participant identifiers, on whose behalf a video chat in the chat can be joined

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getVideoChatAvailableParticipants"] = Field(
        "getVideoChatAvailableParticipants", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
