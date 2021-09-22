# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Hashtags(BaseObject):
    """
    Contains a list of hashtags
    
    :param hashtags: A list of hashtags
    :type hashtags: :class:`list[str]`
    
    """

    ID: str = Field("hashtags", alias="@type")
    hashtags: list[str]

    @staticmethod
    def read(q: dict) -> Hashtags:
        return Hashtags.construct(**q)
