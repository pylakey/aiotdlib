# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetArchivedStories(BaseObject):
    """
    Returns the list of all stories of the current user. The stories are returned in a reverse chronological order (i.e., in order of decreasing story_id). For optimal performance, the number of returned stories is chosen by TDLib

    :param from_story_id: Identifier of the story starting from which stories must be returned; use 0 to get results from the last story
    :type from_story_id: :class:`Int32`
    :param limit: The maximum number of stories to be returned For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getArchivedStories"] = "getArchivedStories"
    from_story_id: Int32
    limit: Int32
