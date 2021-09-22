# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .t_me_url import TMeUrl
from ..base_object import BaseObject


class TMeUrls(BaseObject):
    """
    Contains a list of t.me URLs
    
    :param urls: List of URLs
    :type urls: :class:`list[TMeUrl]`
    
    """

    ID: str = Field("tMeUrls", alias="@type")
    urls: list[TMeUrl]

    @staticmethod
    def read(q: dict) -> TMeUrls:
        return TMeUrls.construct(**q)
