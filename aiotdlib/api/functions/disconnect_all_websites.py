# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DisconnectAllWebsites(BaseObject):
    """
    Disconnects all websites from the current user's Telegram account
    """

    ID: typing.Literal["disconnectAllWebsites"] = "disconnectAllWebsites"
