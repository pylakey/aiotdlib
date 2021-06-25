# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessageLinkInfo(BaseObject):
    """
    Returns information about a public or private message link
    
    Params:
        url (:class:`str`)
            The message link
        
    """

    ID: str = Field("getMessageLinkInfo", alias="@type")
    url: str

    @staticmethod
    def read(q: dict) -> GetMessageLinkInfo:
        return GetMessageLinkInfo.construct(**q)
