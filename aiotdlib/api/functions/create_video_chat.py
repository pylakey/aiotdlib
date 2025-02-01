# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CreateVideoChat(BaseObject):
    """
    Creates a video chat (a group call bound to a chat). Available only for basic groups, supergroups and channels; requires can_manage_video_chats administrator right

    :param chat_id: Identifier of a chat in which the video chat will be created
    :type chat_id: :class:`Int53`
    :param start_date: Point in time (Unix timestamp) when the group call is expected to be started by an administrator; 0 to start the video chat immediately. The date must be at least 10 seconds and at most 8 days in the future
    :type start_date: :class:`Int32`
    :param title: Group call title; if empty, chat title will be used
    :type title: :class:`String`
    :param is_rtmp_stream: Pass true to create an RTMP stream instead of an ordinary video chat
    :type is_rtmp_stream: :class:`Bool`
    """

    ID: typing.Literal["createVideoChat"] = Field("createVideoChat", validation_alias="@type", alias="@type")
    chat_id: Int53
    start_date: Int32
    title: String = ""
    is_rtmp_stream: Bool = False
