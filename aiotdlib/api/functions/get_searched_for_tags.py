# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSearchedForTags(BaseObject):
    """
    Returns recently searched for hashtags or cashtags by their prefix

    :param tag_prefix: Prefix of hashtags or cashtags to return
    :type tag_prefix: :class:`String`
    :param limit: The maximum number of items to be returned
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getSearchedForTags"] = Field("getSearchedForTags", validation_alias="@type", alias="@type")
    tag_prefix: String
    limit: Int32
