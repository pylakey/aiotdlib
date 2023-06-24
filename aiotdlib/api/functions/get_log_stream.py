# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetLogStream(BaseObject):
    """
    Returns information about currently used log stream for internal logging of TDLib. Can be called synchronously
    """

    ID: typing.Literal["getLogStream"] = "getLogStream"
