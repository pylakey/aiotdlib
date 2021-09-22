# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import BackgroundType
from ..types import InputBackground
from ..base_object import BaseObject


class SetBackground(BaseObject):
    """
    Changes the background selected by the user; adds background to the list of installed backgrounds
    
    :param background: The input background to use. Pass null to create a new filled backgrounds. Pass null to remove the current background
    :type background: :class:`InputBackground`
    
    :param type_: Background type. Pass null to use default type of the remote background. Pass null to remove the current background
    :type type_: :class:`BackgroundType`
    
    :param for_dark_theme: True, if the background is chosen for dark theme
    :type for_dark_theme: :class:`bool`
    
    """

    ID: str = Field("setBackground", alias="@type")
    background: InputBackground
    type_: BackgroundType = Field(..., alias='type')
    for_dark_theme: bool

    @staticmethod
    def read(q: dict) -> SetBackground:
        return SetBackground.construct(**q)
