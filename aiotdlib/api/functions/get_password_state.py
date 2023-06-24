# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPasswordState(BaseObject):
    """
    Returns the current state of 2-step verification
    """

    ID: typing.Literal["getPasswordState"] = "getPasswordState"
