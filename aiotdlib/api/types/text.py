# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Text(BaseObject):
    """
    Contains some text
    
    :param text: Text
    :type text: :class:`str`
    
    """

    ID: str = Field("text", alias="@type")
    text: str

    @staticmethod
    def read(q: dict) -> Text:
        return Text.construct(**q)
