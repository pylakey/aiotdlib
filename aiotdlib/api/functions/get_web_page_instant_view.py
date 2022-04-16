# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetWebPageInstantView(BaseObject):
    """
    Returns an instant view version of a web page if available. Returns a 404 error if the web page has no instant view page
    
    :param url: The web page URL
    :type url: :class:`str`
    
    :param force_full: Pass true to get full instant view for the web page
    :type force_full: :class:`bool`
    
    """

    ID: str = Field("getWebPageInstantView", alias="@type")
    url: str
    force_full: bool

    @staticmethod
    def read(q: dict) -> GetWebPageInstantView:
        return GetWebPageInstantView.construct(**q)
