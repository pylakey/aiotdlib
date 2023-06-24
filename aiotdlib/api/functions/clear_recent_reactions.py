# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClearRecentReactions(BaseObject):
    """
    Clears the list of recently used reactions
    """

    ID: typing.Literal["clearRecentReactions"] = "clearRecentReactions"
