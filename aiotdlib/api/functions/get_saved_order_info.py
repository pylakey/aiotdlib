# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSavedOrderInfo(BaseObject):
    """
    Returns saved order information. Returns a 404 error if there is no saved order information
    """

    ID: typing.Literal["getSavedOrderInfo"] = "getSavedOrderInfo"
