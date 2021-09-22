# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class AccountTtl(BaseObject):
    """
    Contains information about the period of inactivity after which the current user's account will automatically be deleted
    
    :param days: Number of days of inactivity before the account will be flagged for deletion; should range from 30-366 days
    :type days: :class:`int`
    
    """

    ID: str = Field("accountTtl", alias="@type")
    days: int

    @staticmethod
    def read(q: dict) -> AccountTtl:
        return AccountTtl.construct(**q)
