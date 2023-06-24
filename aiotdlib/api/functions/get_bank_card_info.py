# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetBankCardInfo(BaseObject):
    """
    Returns information about a bank card

    :param bank_card_number: The bank card number
    :type bank_card_number: :class:`String`
    """

    ID: typing.Literal["getBankCardInfo"] = "getBankCardInfo"
    bank_card_number: String
