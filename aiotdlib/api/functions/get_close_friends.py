# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetCloseFriends(BaseObject):
    """
    Returns all close friends of the current user
    """

    ID: typing.Literal["getCloseFriends"] = "getCloseFriends"
