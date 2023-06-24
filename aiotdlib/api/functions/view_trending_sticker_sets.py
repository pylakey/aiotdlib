# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ViewTrendingStickerSets(BaseObject):
    """
    Informs the server that some trending sticker sets have been viewed by the user

    :param sticker_set_ids: Identifiers of viewed trending sticker sets
    :type sticker_set_ids: :class:`Vector[Int64]`
    """

    ID: typing.Literal["viewTrendingStickerSets"] = "viewTrendingStickerSets"
    sticker_set_ids: Vector[Int64]
