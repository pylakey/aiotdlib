# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSupportUser(BaseObject):
    """
    Returns a user that can be contacted to get support
    """

    ID: typing.Literal["getSupportUser"] = "getSupportUser"
