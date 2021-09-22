# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .bank_card_action_open_url import BankCardActionOpenUrl
from ..base_object import BaseObject


class BankCardInfo(BaseObject):
    """
    Information about a bank card
    
    :param title: Title of the bank card description
    :type title: :class:`str`
    
    :param actions: Actions that can be done with the bank card number
    :type actions: :class:`list[BankCardActionOpenUrl]`
    
    """

    ID: str = Field("bankCardInfo", alias="@type")
    title: str
    actions: list[BankCardActionOpenUrl]

    @staticmethod
    def read(q: dict) -> BankCardInfo:
        return BankCardInfo.construct(**q)
