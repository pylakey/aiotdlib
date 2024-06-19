# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchPublicStoriesByTag(BaseObject):
    """
    Searches for public stories containing the given hashtag or cashtag. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

    :param tag: Hashtag or cashtag to search for
    :type tag: :class:`String`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of stories to be returned; up to 100. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchPublicStoriesByTag"] = Field(
        "searchPublicStoriesByTag", validation_alias="@type", alias="@type"
    )
    tag: String
    offset: String
    limit: Int32