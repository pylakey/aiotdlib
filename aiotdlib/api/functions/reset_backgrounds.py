# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ResetBackgrounds(BaseObject):
    """
    Resets list of installed backgrounds to its default value
    """

    ID: typing.Literal["resetBackgrounds"] = "resetBackgrounds"
