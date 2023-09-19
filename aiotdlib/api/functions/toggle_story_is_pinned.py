# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleStoryIsPinned(BaseObject):
    """
    Toggles whether a story is accessible after expiration

    :param story_id: Identifier of the story
    :type story_id: :class:`Int32`
    :param is_pinned: Pass true to make the story accessible after expiration; pass false to make it private
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["toggleStoryIsPinned"] = "toggleStoryIsPinned"
    story_id: Int32
    is_pinned: Bool = False
