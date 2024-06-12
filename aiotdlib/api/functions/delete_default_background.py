# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteDefaultBackground(BaseObject):
    """
    Deletes default background for chats

    :param for_dark_theme: Pass true if the background is deleted for a dark theme
    :type for_dark_theme: :class:`Bool`
    """

    ID: typing.Literal["deleteDefaultBackground"] = Field(
        "deleteDefaultBackground", validation_alias="@type", alias="@type"
    )
    for_dark_theme: Bool = False
