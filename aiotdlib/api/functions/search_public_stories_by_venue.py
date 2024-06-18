# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchPublicStoriesByVenue(BaseObject):
    """
    Searches for public stories from the given venue. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

    :param venue_provider: Provider of the venue
    :type venue_provider: :class:`String`
    :param venue_id: Identifier of the venue in the provider database
    :type venue_id: :class:`String`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of stories to be returned; up to 100. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchPublicStoriesByVenue"] = Field(
        "searchPublicStoriesByVenue", validation_alias="@type", alias="@type"
    )
    venue_provider: String
    venue_id: String
    offset: String
    limit: Int32
