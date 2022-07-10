# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AssignAppStoreTransaction(BaseObject):
    """
    Informs server about a Telegram Premium purchase through App Store. For official applications only
    
    :param receipt: App Store receipt
    :type receipt: :class:`str`
    
    :param is_restore: Pass true if this is a restore of a Telegram Premium purchase
    :type is_restore: :class:`bool`
    
    """

    ID: str = Field("assignAppStoreTransaction", alias="@type")
    receipt: str
    is_restore: bool

    @staticmethod
    def read(q: dict) -> AssignAppStoreTransaction:
        return AssignAppStoreTransaction.construct(**q)
