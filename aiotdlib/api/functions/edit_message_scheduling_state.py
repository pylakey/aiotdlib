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
    MessageSchedulingState,
)


class EditMessageSchedulingState(BaseObject):
    """
    Edits the time when a scheduled message will be sent. Scheduling state of all messages in the same album or forwarded together with the message will be also changed

    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param scheduling_state: The new message scheduling state; pass null to send the message immediately, defaults to None
    :type scheduling_state: :class:`MessageSchedulingState`, optional
    """

    ID: typing.Literal["editMessageSchedulingState"] = "editMessageSchedulingState"
    chat_id: Int53
    message_id: Int53
    scheduling_state: typing.Optional[MessageSchedulingState] = None
