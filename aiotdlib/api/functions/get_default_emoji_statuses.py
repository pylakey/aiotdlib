# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetDefaultEmojiStatuses(BaseObject):
    """
    Returns default emoji statuses
    """

    ID: typing.Literal["getDefaultEmojiStatuses"] = "getDefaultEmojiStatuses"
