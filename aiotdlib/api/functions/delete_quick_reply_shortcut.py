# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteQuickReplyShortcut(BaseObject):
    """
    Deletes a quick reply shortcut

    :param shortcut_id: Unique identifier of the quick reply shortcut
    :type shortcut_id: :class:`Int32`
    """

    ID: typing.Literal["deleteQuickReplyShortcut"] = Field(
        "deleteQuickReplyShortcut", validation_alias="@type", alias="@type"
    )
    shortcut_id: Int32
