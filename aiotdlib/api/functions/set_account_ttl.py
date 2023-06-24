# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    AccountTtl,
)


class SetAccountTtl(BaseObject):
    """
    Changes the period of inactivity after which the account of the current user will automatically be deleted

    :param ttl: New account TTL
    :type ttl: :class:`AccountTtl`
    """

    ID: typing.Literal["setAccountTtl"] = "setAccountTtl"
    ttl: AccountTtl
