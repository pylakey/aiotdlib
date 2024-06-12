# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatsToSendStories(BaseObject):
    """
    Returns supergroup and channel chats in which the current user has the right to post stories. The chats must be rechecked with canSendStory before actually trying to post a story there
    """

    ID: typing.Literal["getChatsToSendStories"] = Field(
        "getChatsToSendStories", validation_alias="@type", alias="@type"
    )
