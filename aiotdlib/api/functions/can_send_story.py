# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CanSendStory(BaseObject):
    """
    Checks whether the current user can send a story on behalf of a chat; requires can_post_stories right for supergroup and channel chats

    :param chat_id: Chat identifier. Pass Saved Messages chat identifier when posting a story on behalf of the current user
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["canSendStory"] = Field("canSendStory", validation_alias="@type", alias="@type")
    chat_id: Int53
