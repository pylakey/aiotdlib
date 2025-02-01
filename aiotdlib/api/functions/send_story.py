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
    FormattedText,
    InputStoryAreas,
    InputStoryContent,
    StoryFullId,
    StoryPrivacySettings,
)


class SendStory(BaseObject):
    """
    Sends a new story to a chat; requires can_post_stories right for supergroup and channel chats. Returns a temporary story

    :param chat_id: Identifier of the chat that will post the story. Pass Saved Messages chat identifier when posting a story on behalf of the current user
    :type chat_id: :class:`Int53`
    :param content: Content of the story
    :type content: :class:`InputStoryContent`
    :param privacy_settings: The privacy settings for the story; ignored for stories sent to supergroup and channel chats
    :type privacy_settings: :class:`StoryPrivacySettings`
    :param active_period: Period after which the story is moved to archive, in seconds; must be one of 6 * 3600, 12 * 3600, 86400, or 2 * 86400 for Telegram Premium users, and 86400 otherwise
    :type active_period: :class:`Int32`
    :param is_posted_to_chat_page: Pass true to keep the story accessible after expiration
    :type is_posted_to_chat_page: :class:`Bool`
    :param protect_content: Pass true if the content of the story must be protected from forwarding and screenshotting
    :type protect_content: :class:`Bool`
    :param areas: Clickable rectangle areas to be shown on the story media; pass null if none, defaults to None
    :type areas: :class:`InputStoryAreas`, optional
    :param caption: Story caption; pass null to use an empty caption; 0-getOption("story_caption_length_max") characters; can have entities only if getOption("can_use_text_entities_in_story_caption"), defaults to None
    :type caption: :class:`FormattedText`, optional
    :param from_story_full_id: Full identifier of the original story, which content was used to create the story; pass null if the story isn't repost of another story, defaults to None
    :type from_story_full_id: :class:`StoryFullId`, optional
    """

    ID: typing.Literal["sendStory"] = Field("sendStory", validation_alias="@type", alias="@type")
    chat_id: Int53
    content: InputStoryContent
    privacy_settings: StoryPrivacySettings
    active_period: Int32
    is_posted_to_chat_page: Bool = False
    protect_content: Bool = False
    areas: typing.Optional[InputStoryAreas] = None
    caption: typing.Optional[FormattedText] = None
    from_story_full_id: typing.Optional[StoryFullId] = None
