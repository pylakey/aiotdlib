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
    EmojiStatus,
)


class SetEmojiStatus(BaseObject):
    """
    Changes the emoji status of the current user; for Telegram Premium users only

    :param emoji_status: New emoji status; pass null to switch to the default badge, defaults to None
    :type emoji_status: :class:`EmojiStatus`, optional
    """

    ID: typing.Literal["setEmojiStatus"] = "setEmojiStatus"
    emoji_status: typing.Optional[EmojiStatus] = None
