# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetAccountTtl(BaseObject):
    """
    Returns the period of inactivity after which the account of the current user will automatically be deleted
    """

    ID: typing.Literal["getAccountTtl"] = "getAccountTtl"
