# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClearRecentlyFoundChats(BaseObject):
    """
    Clears the list of recently found chats
    """

    ID: typing.Literal["clearRecentlyFoundChats"] = "clearRecentlyFoundChats"
