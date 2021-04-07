# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetLocalizationTargetInfo(BaseObject):
    """
    Returns information about the current localization target. This is an offline request if only_local is true. Can be called before authorization
    
    Params:
        only_local (:class:`bool`)
            If true, returns only locally available information without sending network requests
        
    """

    ID: str = Field("getLocalizationTargetInfo", alias="@type")
    only_local: bool

    @staticmethod
    def read(q: dict) -> GetLocalizationTargetInfo:
        return GetLocalizationTargetInfo.construct(**q)
