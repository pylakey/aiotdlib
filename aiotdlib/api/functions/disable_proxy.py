# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DisableProxy(BaseObject):
    """
    Disables the currently enabled proxy. Can be called before authorization
    
    """

    ID: str = Field("disableProxy", alias="@type")

    @staticmethod
    def read(q: dict) -> DisableProxy:
        return DisableProxy.construct(**q)
