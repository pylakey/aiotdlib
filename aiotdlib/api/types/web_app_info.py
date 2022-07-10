# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class WebAppInfo(BaseObject):
    """
    Contains information about a Web App
    
    :param launch_id: Unique identifier for the Web App launch
    :type launch_id: :class:`int`
    
    :param url: A Web App URL to open in a web view
    :type url: :class:`str`
    
    """

    ID: str = Field("webAppInfo", alias="@type")
    launch_id: int
    url: str

    @staticmethod
    def read(q: dict) -> WebAppInfo:
        return WebAppInfo.construct(**q)
