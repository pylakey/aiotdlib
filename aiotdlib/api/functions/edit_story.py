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
)


class EditStory(BaseObject):
    """
    Changes content and caption of a previously sent story

    :param story_id: Identifier of the story to edit
    :type story_id: :class:`Int32`
    :param content: New content of the story; pass null to keep the current content, defaults to None
    :type content: :class:`InputStoryContent`, optional
    :param areas: New clickable rectangle areas to be shown on the story media; pass null to keep the current areas. Areas can't be edited if story content isn't changed, defaults to None
    :type areas: :class:`InputStoryAreas`, optional
    :param caption: New story caption; pass null to keep the current caption, defaults to None
    :type caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["editStory"] = "editStory"
    story_id: Int32
    content: typing.Optional[InputStoryContent] = None
    areas: typing.Optional[InputStoryAreas] = None
    caption: typing.Optional[FormattedText] = None
