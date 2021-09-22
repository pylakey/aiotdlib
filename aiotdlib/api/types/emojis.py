# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Emojis(BaseObject):
    """
    Represents a list of emoji
    
    :param emojis: List of emojis
    :type emojis: :class:`list[str]`
    
    """

    ID: str = Field("emojis", alias="@type")
    emojis: list[str]

    @staticmethod
    def read(q: dict) -> Emojis:
        return Emojis.construct(**q)
