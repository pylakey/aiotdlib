# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class OpenStory(BaseObject):
    """
    Informs TDLib that a story is opened and is being viewed by the user

    :param story_sender_chat_id: The identifier of the sender of the opened story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: The identifier of the story
    :type story_id: :class:`Int32`
    """

    ID: typing.Literal["openStory"] = "openStory"
    story_sender_chat_id: Int53
    story_id: Int32
