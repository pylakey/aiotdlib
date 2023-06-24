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
    MessageAutoDeleteTime,
)


class SetDefaultMessageAutoDeleteTime(BaseObject):
    """
    Changes the default message auto-delete time for new chats

    :param message_auto_delete_time: New default message auto-delete time; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
    :type message_auto_delete_time: :class:`MessageAutoDeleteTime`
    """

    ID: typing.Literal["setDefaultMessageAutoDeleteTime"] = "setDefaultMessageAutoDeleteTime"
    message_auto_delete_time: MessageAutoDeleteTime = 0
