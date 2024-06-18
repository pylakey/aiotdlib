# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClearSearchedForTags(BaseObject):
    """
    Clears the list of recently searched for hashtags or cashtags

    :param clear_cashtags: Pass true to clear the list of recently searched for cashtags; otherwise, the list of recently searched for hashtags will be cleared
    :type clear_cashtags: :class:`Bool`
    """

    ID: typing.Literal["clearSearchedForTags"] = Field("clearSearchedForTags", validation_alias="@type", alias="@type")
    clear_cashtags: Bool = False
