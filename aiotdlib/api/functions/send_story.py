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
    StoryPrivacySettings,
)


class SendStory(BaseObject):
    """
    Sends a new story. Returns a temporary story

    :param content: Content of the story
    :type content: :class:`InputStoryContent`
    :param privacy_settings: The privacy settings for the story
    :type privacy_settings: :class:`StoryPrivacySettings`
    :param active_period: Period after which the story is moved to archive, in seconds; must be one of 6 * 3600, 12 * 3600, 86400, or 2 * 86400 for Telegram Premium users, and 86400 otherwise
    :type active_period: :class:`Int32`
    :param is_pinned: Pass true to keep the story accessible after expiration
    :type is_pinned: :class:`Bool`
    :param protect_content: Pass true if the content of the story must be protected from forwarding and screenshotting
    :type protect_content: :class:`Bool`
    :param areas: Clickable rectangle areas to be shown on the story media; pass null if none, defaults to None
    :type areas: :class:`InputStoryAreas`, optional
    :param caption: Story caption; pass null to use an empty caption; 0-getOption("story_caption_length_max") characters, defaults to None
    :type caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["sendStory"] = "sendStory"
    content: InputStoryContent
    privacy_settings: StoryPrivacySettings
    active_period: Int32
    is_pinned: Bool = False
    protect_content: Bool = False
    areas: typing.Optional[InputStoryAreas] = None
    caption: typing.Optional[FormattedText] = None
