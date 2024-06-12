# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckQuickReplyShortcutName(BaseObject):
    """
    Checks validness of a name for a quick reply shortcut. Can be called synchronously

    :param name: The name of the shortcut; 1-32 characters
    :type name: :class:`String`
    """

    ID: typing.Literal["checkQuickReplyShortcutName"] = Field(
        "checkQuickReplyShortcutName", validation_alias="@type", alias="@type"
    )
    name: String = Field(..., min_length=1, max_length=32)
