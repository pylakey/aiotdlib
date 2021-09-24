# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetAccountTtl(BaseObject):
    """
    Returns the period of inactivity after which the account of the current user will automatically be deleted
    
    """

    ID: str = Field("getAccountTtl", alias="@type")

    @staticmethod
    def read(q: dict) -> GetAccountTtl:
        return GetAccountTtl.construct(**q)
