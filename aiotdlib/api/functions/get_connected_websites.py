# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetConnectedWebsites(BaseObject):
    """
    Returns all website where the current user used Telegram to log in
    """

    ID: typing.Literal["getConnectedWebsites"] = "getConnectedWebsites"
