# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class LoadQuickReplyShortcutMessages(BaseObject):
    """
    Loads quick reply messages that can be sent by a given quick reply shortcut. The loaded messages will be sent through updateQuickReplyShortcutMessages

    :param shortcut_id: Unique identifier of the quick reply shortcut
    :type shortcut_id: :class:`Int32`
    """

    ID: typing.Literal["loadQuickReplyShortcutMessages"] = Field(
        "loadQuickReplyShortcutMessages", validation_alias="@type", alias="@type"
    )
    shortcut_id: Int32
