# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DisableProxy(BaseObject):
    """
    Disables the currently enabled proxy. Can be called before authorization
    """

    ID: typing.Literal["disableProxy"] = "disableProxy"
