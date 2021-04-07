# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import AccountTtl


class SetAccountTtl(BaseObject):
    """
    Changes the period of inactivity after which the account of the current user will automatically be deleted
    
    Params:
        ttl (:class:`AccountTtl`)
            New account TTL
        
    """

    ID: str = Field("setAccountTtl", alias="@type")
    ttl: AccountTtl

    @staticmethod
    def read(q: dict) -> SetAccountTtl:
        return SetAccountTtl.construct(**q)
