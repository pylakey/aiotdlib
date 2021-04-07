# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .connected_website import ConnectedWebsite
from ..base_object import BaseObject


class ConnectedWebsites(BaseObject):
    """
    Contains a list of websites the current user is logged in with Telegram
    
    Params:
        websites (:obj:`list[ConnectedWebsite]`)
            List of connected websites
        
    """

    ID: str = Field("connectedWebsites", alias="@type")
    websites: list[ConnectedWebsite]

    @staticmethod
    def read(q: dict) -> ConnectedWebsites:
        return ConnectedWebsites.construct(**q)
