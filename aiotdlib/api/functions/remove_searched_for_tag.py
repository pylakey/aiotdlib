# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RemoveSearchedForTag(BaseObject):
    """
    Removes a hashtag or a cashtag from the list of recently searched for hashtags or cashtags

    :param tag: Hashtag or cashtag to delete
    :type tag: :class:`String`
    """

    ID: typing.Literal["removeSearchedForTag"] = Field("removeSearchedForTag", validation_alias="@type", alias="@type")
    tag: String
