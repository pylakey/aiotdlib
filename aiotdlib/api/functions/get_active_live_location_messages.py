# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetActiveLiveLocationMessages(BaseObject):
    """
    Returns all active live locations that need to be updated by the application. The list is persistent across application restarts only if the message database is used
    """

    ID: typing.Literal["getActiveLiveLocationMessages"] = "getActiveLiveLocationMessages"
