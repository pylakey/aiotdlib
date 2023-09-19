# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPollVoters(BaseObject):
    """
    Returns message senders voted for the specified option in a non-anonymous polls. For optimal performance, the number of returned users is chosen by TDLib

    :param chat_id: Identifier of the chat to which the poll belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message containing the poll
    :type message_id: :class:`Int53`
    :param option_id: 0-based identifier of the answer option
    :type option_id: :class:`Int32`
    :param offset: Number of voters to skip in the result; must be non-negative
    :type offset: :class:`Int32`
    :param limit: The maximum number of voters to be returned; must be positive and can't be greater than 50. For optimal performance, the number of returned voters is chosen by TDLib and can be smaller than the specified limit, even if the end of the voter list has not been reached
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getPollVoters"] = "getPollVoters"
    chat_id: Int53
    message_id: Int53
    option_id: Int32
    offset: Int32
    limit: Int32
