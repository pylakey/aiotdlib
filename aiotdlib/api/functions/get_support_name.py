# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSupportName(BaseObject):
    """
    Returns localized name of the Telegram support user; for Telegram support only
    """

    ID: typing.Literal["getSupportName"] = "getSupportName"
