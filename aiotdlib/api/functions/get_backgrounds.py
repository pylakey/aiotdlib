# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetBackgrounds(BaseObject):
    """
    Returns backgrounds installed by the user

    :param for_dark_theme: Pass true to order returned backgrounds for a dark theme
    :type for_dark_theme: :class:`Bool`
    """

    ID: typing.Literal["getBackgrounds"] = "getBackgrounds"
    for_dark_theme: Bool = False
