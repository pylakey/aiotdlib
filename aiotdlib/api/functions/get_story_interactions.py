# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStoryInteractions(BaseObject):
    """
    Returns interactions with a story. The method can be called only for stories posted on behalf of the current user

    :param story_id: Story identifier
    :type story_id: :class:`Int32`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of story interactions to return
    :type limit: :class:`Int32`
    :param query: Query to search for in names, usernames and titles; may be empty to get all relevant interactions
    :type query: :class:`String`
    :param only_contacts: Pass true to get only interactions by contacts; pass false to get all relevant interactions
    :type only_contacts: :class:`Bool`
    :param prefer_forwards: Pass true to get forwards and reposts first, then reactions, then other views; pass false to get interactions sorted just by interaction date
    :type prefer_forwards: :class:`Bool`
    :param prefer_with_reaction: Pass true to get interactions with reaction first; pass false to get interactions sorted just by interaction date. Ignored if prefer_forwards == true
    :type prefer_with_reaction: :class:`Bool`
    """

    ID: typing.Literal["getStoryInteractions"] = Field("getStoryInteractions", validation_alias="@type", alias="@type")
    story_id: Int32
    offset: String
    limit: Int32
    query: String = ""
    only_contacts: Bool = False
    prefer_forwards: Bool = False
    prefer_with_reaction: Bool = False
