# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchHashtags(BaseObject):
    """
    Searches for recently used hashtags by their prefix

    :param prefix: Hashtag prefix to search for
    :type prefix: :class:`String`
    :param limit: The maximum number of hashtags to be returned
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchHashtags"] = Field("searchHashtags", validation_alias="@type", alias="@type")
    prefix: String
    limit: Int32
