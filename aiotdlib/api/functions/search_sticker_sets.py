# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchStickerSets(BaseObject):
    """
    Searches for ordinary sticker sets by looking for specified query in their title and name. Excludes installed sticker sets from the results

    :param query: Query to search for
    :type query: :class:`String`
    """

    ID: typing.Literal["searchStickerSets"] = "searchStickerSets"
    query: String
