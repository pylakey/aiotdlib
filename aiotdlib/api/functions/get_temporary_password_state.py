# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetTemporaryPasswordState(BaseObject):
    """
    Returns information about the current temporary password
    """

    ID: typing.Literal["getTemporaryPasswordState"] = "getTemporaryPasswordState"
