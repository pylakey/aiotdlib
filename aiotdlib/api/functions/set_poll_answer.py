# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetPollAnswer(BaseObject):
    """
    Changes the user answer to a poll. A poll in quiz mode can be answered only once

    :param chat_id: Identifier of the chat to which the poll belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message containing the poll
    :type message_id: :class:`Int53`
    :param option_ids: 0-based identifiers of answer options, chosen by the user. User can choose more than 1 answer option only is the poll allows multiple answers
    :type option_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["setPollAnswer"] = "setPollAnswer"
    chat_id: Int53
    message_id: Int53
    option_ids: Vector[Int32]
