# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetLogTagVerbosityLevel(BaseObject):
    """
    Returns current verbosity level for a specified TDLib internal log tag. Can be called synchronously

    :param tag: Logging tag to change verbosity level
    :type tag: :class:`String`
    """

    ID: typing.Literal["getLogTagVerbosityLevel"] = "getLogTagVerbosityLevel"
    tag: String
