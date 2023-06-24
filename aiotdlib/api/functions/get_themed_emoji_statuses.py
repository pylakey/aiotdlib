# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetThemedEmojiStatuses(BaseObject):
    """
    Returns up to 8 emoji statuses, which must be shown right after the default Premium Badge in the emoji status list
    """

    ID: typing.Literal["getThemedEmojiStatuses"] = "getThemedEmojiStatuses"
