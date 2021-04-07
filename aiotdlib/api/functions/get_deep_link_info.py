# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetDeepLinkInfo(BaseObject):
    """
    Returns information about a tg:// deep link. Use "tg://need_update_for_some_feature" or "tg:some_unsupported_feature" for testing. Returns a 404 error for unknown links. Can be called before authorization
    
    Params:
        link (:class:`str`)
            The link
        
    """

    ID: str = Field("getDeepLinkInfo", alias="@type")
    link: str

    @staticmethod
    def read(q: dict) -> GetDeepLinkInfo:
        return GetDeepLinkInfo.construct(**q)
