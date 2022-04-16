# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import BackgroundType
from ..types import InputBackground


class SetBackground(BaseObject):
    """
    Changes the background selected by the user; adds background to the list of installed backgrounds
    
    :param background: The input background to use; pass null to create a new filled backgrounds or to remove the current background
    :type background: :class:`InputBackground`
    
    :param type_: Background type; pass null to use the default type of the remote background or to remove the current background
    :type type_: :class:`BackgroundType`
    
    :param for_dark_theme: Pass true if the background is changed for a dark theme
    :type for_dark_theme: :class:`bool`
    
    """

    ID: str = Field("setBackground", alias="@type")
    background: InputBackground
    type_: BackgroundType = Field(..., alias='type')
    for_dark_theme: bool

    @staticmethod
    def read(q: dict) -> SetBackground:
        return SetBackground.construct(**q)
