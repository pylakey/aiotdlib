# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetExternalLinkInfo(BaseObject):
    """
    Returns information about an action to be done when the current user clicks an HTTP link. This method can be used to automatically authorize the current user on a website. Don't use this method for links from secret chats if link preview is disabled in secret chats
    
    Params:
        link (:class:`str`)
            The HTTP link
        
    """

    ID: str = Field("getExternalLinkInfo", alias="@type")
    link: str

    @staticmethod
    def read(q: dict) -> GetExternalLinkInfo:
        return GetExternalLinkInfo.construct(**q)
