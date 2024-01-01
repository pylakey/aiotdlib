# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetRecentStickers(BaseObject):
    """
    Returns a list of recently used stickers

    :param is_attached: Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers
    :type is_attached: :class:`Bool`
    """

    ID: typing.Literal["getRecentStickers"] = Field("getRecentStickers", validation_alias="@type", alias="@type")
    is_attached: Bool = False
