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
    ChatLocation,
)


class CreateNewSupergroupChat(BaseObject):
    """
    Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate. Returns the newly created chat

    :param title: Title of the new chat; 1-128 characters
    :type title: :class:`String`
    :param is_forum: Pass true to create a forum supergroup chat
    :type is_forum: :class:`Bool`
    :param is_channel: Pass true to create a channel chat; ignored if a forum is created
    :type is_channel: :class:`Bool`
    :param description: Chat description; 0-255 characters
    :type description: :class:`String`
    :param message_auto_delete_time: Message auto-delete time value, in seconds; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
    :type message_auto_delete_time: :class:`Int32`
    :param for_import: Pass true to create a supergroup for importing messages using importMessage
    :type for_import: :class:`Bool`
    :param location: Chat location if a location-based supergroup is being created; pass null to create an ordinary supergroup chat, defaults to None
    :type location: :class:`ChatLocation`, optional
    """

    ID: typing.Literal["createNewSupergroupChat"] = "createNewSupergroupChat"
    title: String = Field(..., min_length=1, max_length=128)
    is_forum: Bool = False
    is_channel: Bool = False
    description: String = Field("", max_length=255)
    message_auto_delete_time: Int32 = 0
    for_import: Bool = False
    location: typing.Optional[ChatLocation] = None
