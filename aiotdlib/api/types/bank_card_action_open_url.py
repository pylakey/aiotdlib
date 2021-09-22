# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class BankCardActionOpenUrl(BaseObject):
    """
    Describes an action associated with a bank card number
    
    :param text: Action text
    :type text: :class:`str`
    
    :param url: The URL to be opened
    :type url: :class:`str`
    
    """

    ID: str = Field("bankCardActionOpenUrl", alias="@type")
    text: str
    url: str

    @staticmethod
    def read(q: dict) -> BankCardActionOpenUrl:
        return BankCardActionOpenUrl.construct(**q)
