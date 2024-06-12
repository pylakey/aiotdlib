# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStoryStatistics(BaseObject):
    """
    Returns detailed statistics about a story. Can be used only if story.can_get_statistics == true

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param story_id: Story identifier
    :type story_id: :class:`Int32`
    :param is_dark: Pass true if a dark theme is used by the application
    :type is_dark: :class:`Bool`
    """

    ID: typing.Literal["getStoryStatistics"] = Field("getStoryStatistics", validation_alias="@type", alias="@type")
    chat_id: Int53
    story_id: Int32
    is_dark: Bool = False
