# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import AccountTtl
from ..base_object import BaseObject


class SetAccountTtl(BaseObject):
    """
    Changes the period of inactivity after which the account of the current user will automatically be deleted
    
    :param ttl: New account TTL
    :type ttl: :class:`AccountTtl`
    
    """

    ID: str = Field("setAccountTtl", alias="@type")
    ttl: AccountTtl

    @staticmethod
    def read(q: dict) -> SetAccountTtl:
        return SetAccountTtl.construct(**q)
