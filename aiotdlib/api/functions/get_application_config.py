# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetApplicationConfig(BaseObject):
    """
    Returns application config, provided by the server. Can be called before authorization
    
    """

    ID: str = Field("getApplicationConfig", alias="@type")

    @staticmethod
    def read(q: dict) -> GetApplicationConfig:
        return GetApplicationConfig.construct(**q)
