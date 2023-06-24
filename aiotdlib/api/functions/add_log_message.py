# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AddLogMessage(BaseObject):
    """
    Adds a message to TDLib internal log. Can be called synchronously

    :param verbosity_level: The minimum verbosity level needed for the message to be logged; 0-1023
    :type verbosity_level: :class:`Int32`
    :param text: Text of a message to log
    :type text: :class:`String`
    """

    ID: typing.Literal["addLogMessage"] = "addLogMessage"
    verbosity_level: Int32
    text: String
