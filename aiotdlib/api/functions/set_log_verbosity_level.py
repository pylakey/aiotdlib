# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetLogVerbosityLevel(BaseObject):
    """
    Sets the verbosity level of the internal logging of TDLib. Can be called synchronously

    :param new_verbosity_level: New value of the verbosity level for logging. Value 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings, value 3 corresponds to informational, value 4 corresponds to debug, value 5 corresponds to verbose debug, value greater than 5 and up to 1023 can be used to enable even more logging
    :type new_verbosity_level: :class:`Int32`
    """

    ID: typing.Literal["setLogVerbosityLevel"] = "setLogVerbosityLevel"
    new_verbosity_level: Int32
