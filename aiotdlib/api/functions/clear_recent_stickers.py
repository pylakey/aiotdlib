# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClearRecentStickers(BaseObject):
    """
    Clears the list of recently used stickers

    :param is_attached: Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers
    :type is_attached: :class:`Bool`
    """

    ID: typing.Literal["clearRecentStickers"] = "clearRecentStickers"
    is_attached: Bool = False
