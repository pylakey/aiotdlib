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
    StoryPrivacySettings,
)


class SetStoryPrivacySettings(BaseObject):
    """
    Changes privacy settings of a previously sent story

    :param story_id: Identifier of the story
    :type story_id: :class:`Int32`
    :param privacy_settings: The new privacy settigs for the story
    :type privacy_settings: :class:`StoryPrivacySettings`
    """

    ID: typing.Literal["setStoryPrivacySettings"] = "setStoryPrivacySettings"
    story_id: Int32
    privacy_settings: StoryPrivacySettings
