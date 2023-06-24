# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetDefaultMessageAutoDeleteTime(BaseObject):
    """
    Returns default message auto-delete time setting for new chats
    """

    ID: typing.Literal["getDefaultMessageAutoDeleteTime"] = "getDefaultMessageAutoDeleteTime"
