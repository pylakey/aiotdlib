# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatBoostFeatures(BaseObject):
    """
    Returns the list of features available for different chat boost levels. This is an offline method

    :param is_channel: Pass true to get the list of features for channels; pass false to get the list of features for supergroups
    :type is_channel: :class:`Bool`
    """

    ID: typing.Literal["getChatBoostFeatures"] = Field("getChatBoostFeatures", validation_alias="@type", alias="@type")
    is_channel: Bool = False
