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
    StarTransactionDirection,
)


class GetStarTransactions(BaseObject):
    """
    Returns the list of Telegram star transactions for the current user

    :param offset: Offset of the first transaction to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param direction: Direction of the transactions to receive; pass null to get all transactions, defaults to None
    :type direction: :class:`StarTransactionDirection`, optional
    """

    ID: typing.Literal["getStarTransactions"] = Field("getStarTransactions", validation_alias="@type", alias="@type")
    offset: String
    direction: typing.Optional[StarTransactionDirection] = None
