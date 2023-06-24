# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetRecentInlineBots(BaseObject):
    """
    Returns up to 20 recently used inline bots in the order of their last usage
    """

    ID: typing.Literal["getRecentInlineBots"] = "getRecentInlineBots"
