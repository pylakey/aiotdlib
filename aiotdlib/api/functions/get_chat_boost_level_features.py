# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatBoostLevelFeatures(BaseObject):
    """
    Returns the list of features available on the specific chat boost level. This is an offline method

    :param level: Chat boost level
    :type level: :class:`Int32`
    :param is_channel: Pass true to get the list of features for channels; pass false to get the list of features for supergroups
    :type is_channel: :class:`Bool`
    """

    ID: typing.Literal["getChatBoostLevelFeatures"] = Field(
        "getChatBoostLevelFeatures", validation_alias="@type", alias="@type"
    )
    level: Int32
    is_channel: Bool = False
