# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetBankCardInfo(BaseObject):
    """
    Returns information about a bank card
    
    :param bank_card_number: The bank card number
    :type bank_card_number: :class:`str`
    
    """

    ID: str = Field("getBankCardInfo", alias="@type")
    bank_card_number: str

    @staticmethod
    def read(q: dict) -> GetBankCardInfo:
        return GetBankCardInfo.construct(**q)
