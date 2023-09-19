# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteStory(BaseObject):
    """
    Deletes a previously sent story

    :param story_id: Identifier of the story to delete
    :type story_id: :class:`Int32`
    """

    ID: typing.Literal["deleteStory"] = "deleteStory"
    story_id: Int32
