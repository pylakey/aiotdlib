# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClearRecentEmojiStatuses(BaseObject):
    """
    Clears the list of recently used emoji statuses
    """

    ID: typing.Literal["clearRecentEmojiStatuses"] = "clearRecentEmojiStatuses"
