# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ThemeParameters


class GetWebAppUrl(BaseObject):
    """
    Returns an HTTPS URL of a Web App to open after keyboardButtonTypeWebApp button is pressed
    
    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`int`
    
    :param url: The URL from the keyboardButtonTypeWebApp button
    :type url: :class:`str`
    
    :param theme: Preferred Web App theme; pass null to use the default theme
    :type theme: :class:`ThemeParameters`
    
    """

    ID: str = Field("getWebAppUrl", alias="@type")
    bot_user_id: int
    url: str
    theme: ThemeParameters

    @staticmethod
    def read(q: dict) -> GetWebAppUrl:
        return GetWebAppUrl.construct(**q)
