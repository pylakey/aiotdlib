# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetExternalLinkInfo(BaseObject):
    """
    Returns information about an action to be done when the current user clicks an external link. Don't use this method for links from secret chats if web page preview is disabled in secret chats
    
    :param link: The link
    :type link: :class:`str`
    
    """

    ID: str = Field("getExternalLinkInfo", alias="@type")
    link: str

    @staticmethod
    def read(q: dict) -> GetExternalLinkInfo:
        return GetExternalLinkInfo.construct(**q)
