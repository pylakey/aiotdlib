# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetApplicationDownloadLink(BaseObject):
    """
    Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram
    
    """

    ID: str = Field("getApplicationDownloadLink", alias="@type")

    @staticmethod
    def read(q: dict) -> GetApplicationDownloadLink:
        return GetApplicationDownloadLink.construct(**q)
