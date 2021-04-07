# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetExternalLink(BaseObject):
    """
    Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed
    
    Params:
        link (:class:`str`)
            The HTTP link
        
        allow_write_access (:class:`bool`)
            True, if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages
        
    """

    ID: str = Field("getExternalLink", alias="@type")
    link: str
    allow_write_access: bool

    @staticmethod
    def read(q: dict) -> GetExternalLink:
        return GetExternalLink.construct(**q)
