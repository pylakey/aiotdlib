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
    
    :param only_local: Pass true to get only locally available information without sending network requests
    :type only_local: :class:`bool`
    
    """

    ID: str = Field("getLocalizationTargetInfo", alias="@type")
    only_local: bool

    @staticmethod
    def read(q: dict) -> GetLocalizationTargetInfo:
        return GetLocalizationTargetInfo.construct(**q)
