# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CloseWebApp(BaseObject):
    """
    Informs TDLib that a previously opened Web App was closed
    
    :param web_app_launch_id: Identifier of Web App launch, received from openWebApp
    :type web_app_launch_id: :class:`int`
    
    """

    ID: str = Field("closeWebApp", alias="@type")
    web_app_launch_id: int

    @staticmethod
    def read(q: dict) -> CloseWebApp:
        return CloseWebApp.construct(**q)
