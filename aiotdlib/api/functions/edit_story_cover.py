# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class EditStoryCover(BaseObject):
    """
    Changes cover of a video story. Can be called only if story.can_be_edited == true and the story isn't being edited now

    :param story_sender_chat_id: Identifier of the chat that posted the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: Identifier of the story to edit
    :type story_id: :class:`Int32`
    :param cover_frame_timestamp: New timestamp of the frame, which will be used as video thumbnail
    :type cover_frame_timestamp: :class:`Double`
    """

    ID: typing.Literal["editStoryCover"] = Field("editStoryCover", validation_alias="@type", alias="@type")
    story_sender_chat_id: Int53
    story_id: Int32
    cover_frame_timestamp: Double
