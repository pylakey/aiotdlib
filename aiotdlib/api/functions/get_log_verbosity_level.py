# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetLogVerbosityLevel(BaseObject):
    """
    Returns current verbosity level of the internal logging of TDLib. Can be called synchronously
    """

    ID: typing.Literal["getLogVerbosityLevel"] = "getLogVerbosityLevel"
