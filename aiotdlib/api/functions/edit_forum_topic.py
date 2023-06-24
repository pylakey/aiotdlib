# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class EditForumTopic(BaseObject):
    """
    Edits title and icon of a topic in a forum supergroup chat; requires can_manage_topics administrator right in the supergroup unless the user is creator of the topic

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`Int53`
    :param icon_custom_emoji_id: Identifier of the new custom emoji for topic icon; pass 0 to remove the custom emoji. Ignored if edit_icon_custom_emoji is false. Telegram Premium users can use any custom emoji, other users can use only a custom emoji returned by getForumTopicDefaultIcons
    :type icon_custom_emoji_id: :class:`Int64`
    :param name: New name of the topic; 0-128 characters. If empty, the previous topic name is kept
    :type name: :class:`String`
    :param edit_icon_custom_emoji: Pass true to edit the icon of the topic. Icon of the General topic can't be edited
    :type edit_icon_custom_emoji: :class:`Bool`
    """

    ID: typing.Literal["editForumTopic"] = "editForumTopic"
    chat_id: Int53
    message_thread_id: Int53
    icon_custom_emoji_id: Int64
    name: String = Field("", max_length=128)
    edit_icon_custom_emoji: Bool = False
