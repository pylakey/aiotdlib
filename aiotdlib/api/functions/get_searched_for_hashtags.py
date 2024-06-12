# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSearchedForHashtags(BaseObject):
    """
    Returns recently searched for hashtags or cashtags by their prefix

    :param prefix: Prefix of hashtags or cashtags to return
    :type prefix: :class:`String`
    :param limit: The maximum number of items to be returned
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getSearchedForHashtags"] = Field(
        "getSearchedForHashtags", validation_alias="@type", alias="@type"
    )
    prefix: String
    limit: Int32
