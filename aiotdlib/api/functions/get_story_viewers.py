# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStoryViewers(BaseObject):
    """
    Returns viewers of a story. The method can be called if story.can_get_viewers == true

    :param story_id: Story identifier
    :type story_id: :class:`Int32`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of story viewers to return
    :type limit: :class:`Int32`
    :param query: Query to search for in names and usernames of the viewers; may be empty to get all relevant viewers
    :type query: :class:`String`
    :param only_contacts: Pass true to get only contacts; pass false to get all relevant viewers
    :type only_contacts: :class:`Bool`
    :param prefer_with_reaction: Pass true to get viewers with reaction first; pass false to get viewers sorted just by view_date
    :type prefer_with_reaction: :class:`Bool`
    """

    ID: typing.Literal["getStoryViewers"] = "getStoryViewers"
    story_id: Int32
    offset: String
    limit: Int32
    query: String = ""
    only_contacts: Bool = False
    prefer_with_reaction: Bool = False
