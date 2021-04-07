# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .bank_card_action_open_url import BankCardActionOpenUrl
from ..base_object import BaseObject


class BankCardInfo(BaseObject):
    """
    Information about a bank card
    
    Params:
        title (:class:`str`)
            Title of the bank card description
        
        actions (:obj:`list[BankCardActionOpenUrl]`)
            Actions that can be done with the bank card number
        
    """

    ID: str = Field("bankCardInfo", alias="@type")
    title: str
    actions: list[BankCardActionOpenUrl]

    @staticmethod
    def read(q: dict) -> BankCardInfo:
        return BankCardInfo.construct(**q)
