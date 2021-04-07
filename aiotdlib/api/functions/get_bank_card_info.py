# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetBankCardInfo(BaseObject):
    """
    Returns information about a bank card
    
    Params:
        bank_card_number (:class:`str`)
            The bank card number
        
    """

    ID: str = Field("getBankCardInfo", alias="@type")
    bank_card_number: str

    @staticmethod
    def read(q: dict) -> GetBankCardInfo:
        return GetBankCardInfo.construct(**q)
