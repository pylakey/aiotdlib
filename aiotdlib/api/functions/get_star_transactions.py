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
    MessageSender,
    StarTransactionDirection,
)


class GetStarTransactions(BaseObject):
    """
    Returns the list of Telegram star transactions for the specified owner

    :param owner_id: Identifier of the owner of the Telegram stars; can be the identifier of the current user, identifier of an owned bot, or identifier of a channel chat with supergroupFullInfo.can_get_revenue_statistics == true
    :type owner_id: :class:`MessageSender`
    :param offset: Offset of the first transaction to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of transactions to return
    :type limit: :class:`Int32`
    :param direction: Direction of the transactions to receive; pass null to get all transactions, defaults to None
    :type direction: :class:`StarTransactionDirection`, optional
    """

    ID: typing.Literal["getStarTransactions"] = Field("getStarTransactions", validation_alias="@type", alias="@type")
    owner_id: MessageSender
    offset: String
    limit: Int32
    direction: typing.Optional[StarTransactionDirection] = None
