# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .background import Background
from ..base_object import BaseObject


class Backgrounds(BaseObject):
    """
    Contains a list of backgrounds
    
    :param backgrounds: A list of backgrounds
    :type backgrounds: :class:`list[Background]`
    
    """

    ID: str = Field("backgrounds", alias="@type")
    backgrounds: list[Background]

    @staticmethod
    def read(q: dict) -> Backgrounds:
        return Backgrounds.construct(**q)
