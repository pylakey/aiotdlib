# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteQuickReplyShortcutMessages(BaseObject):
    """
    Deletes specified quick reply messages

    :param shortcut_id: Unique identifier of the quick reply shortcut to which the messages belong
    :type shortcut_id: :class:`Int32`
    :param message_ids: Unique identifiers of the messages
    :type message_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["deleteQuickReplyShortcutMessages"] = Field(
        "deleteQuickReplyShortcutMessages", validation_alias="@type", alias="@type"
    )
    shortcut_id: Int32
    message_ids: Vector[Int53]
