# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetFavoriteStickers(BaseObject):
    """
    Returns favorite stickers
    """

    ID: typing.Literal["getFavoriteStickers"] = "getFavoriteStickers"
