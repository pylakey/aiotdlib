# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AccountTtl(BaseObject):
    """
    Contains information about the period of inactivity after which the current user's account will automatically be deleted
    
    Params:
        days (:class:`int`)
            Number of days of inactivity before the account will be flagged for deletion; should range from 30-366 days
        
    """

    ID: str = Field("accountTtl", alias="@type")
    days: int

    @staticmethod
    def read(q: dict) -> AccountTtl:
        return AccountTtl.construct(**q)
