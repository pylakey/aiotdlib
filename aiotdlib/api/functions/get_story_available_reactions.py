# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStoryAvailableReactions(BaseObject):
    """
    Returns reactions, which can be chosen for a story

    :param row_size: Number of reaction per row, 5-25
    :type row_size: :class:`Int32`
    """

    ID: typing.Literal["getStoryAvailableReactions"] = "getStoryAvailableReactions"
    row_size: Int32
