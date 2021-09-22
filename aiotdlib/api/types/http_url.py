# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class HttpUrl(BaseObject):
    """
    Contains an HTTP URL
    
    :param url: The URL
    :type url: :class:`str`
    
    """

    ID: str = Field("httpUrl", alias="@type")
    url: str

    @staticmethod
    def read(q: dict) -> HttpUrl:
        return HttpUrl.construct(**q)
