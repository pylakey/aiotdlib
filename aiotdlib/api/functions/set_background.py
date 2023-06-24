# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    BackgroundType,
    InputBackground,
)


class SetBackground(BaseObject):
    """
    Changes the background selected by the user; adds background to the list of installed backgrounds

    :param for_dark_theme: Pass true if the background is changed for a dark theme
    :type for_dark_theme: :class:`Bool`
    :param background: The input background to use; pass null to create a new filled background or to remove the current background, defaults to None
    :type background: :class:`InputBackground`, optional
    :param type_: Background type; pass null to use the default type of the remote background or to remove the current background, defaults to None
    :type type_: :class:`BackgroundType`, optional
    """

    ID: typing.Literal["setBackground"] = "setBackground"
    for_dark_theme: Bool = False
    background: typing.Optional[InputBackground] = None
    type_: typing.Optional[BackgroundType] = Field(None, alias="type")
