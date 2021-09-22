# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetExternalLink(BaseObject):
    """
    Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed
    
    :param link: The HTTP link
    :type link: :class:`str`
    
    :param allow_write_access: True, if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages
    :type allow_write_access: :class:`bool`
    
    """

    ID: str = Field("getExternalLink", alias="@type")
    link: str
    allow_write_access: bool

    @staticmethod
    def read(q: dict) -> GetExternalLink:
        return GetExternalLink.construct(**q)
