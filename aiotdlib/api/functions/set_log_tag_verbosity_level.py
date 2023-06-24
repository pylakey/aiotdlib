# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetLogTagVerbosityLevel(BaseObject):
    """
    Sets the verbosity level for a specified TDLib internal log tag. Can be called synchronously

    :param tag: Logging tag to change verbosity level
    :type tag: :class:`String`
    :param new_verbosity_level: New verbosity level; 1-1024
    :type new_verbosity_level: :class:`Int32`
    """

    ID: typing.Literal["setLogTagVerbosityLevel"] = "setLogTagVerbosityLevel"
    tag: String
    new_verbosity_level: Int32
