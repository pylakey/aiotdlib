# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class BankCardActionOpenUrl(BaseObject):
    """
    Describes an action associated with a bank card number
    
    Params:
        text (:class:`str`)
            Action text
        
        url (:class:`str`)
            The URL to be opened
        
    """

    ID: str = Field("bankCardActionOpenUrl", alias="@type")
    text: str
    url: str

    @staticmethod
    def read(q: dict) -> BankCardActionOpenUrl:
        return BankCardActionOpenUrl.construct(**q)
