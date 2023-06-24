# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CanTransferOwnership(BaseObject):
    """
    Checks whether the current session can be used to transfer a chat ownership to another user
    """

    ID: typing.Literal["canTransferOwnership"] = "canTransferOwnership"
