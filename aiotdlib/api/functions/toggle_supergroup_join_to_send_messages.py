# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleSupergroupJoinToSendMessages(BaseObject):
    """
    Toggles whether joining is mandatory to send messages to a discussion supergroup; requires can_restrict_members administrator right

    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`Int53`
    :param join_to_send_messages: New value of join_to_send_messages
    :type join_to_send_messages: :class:`Bool`
    """

    ID: typing.Literal["toggleSupergroupJoinToSendMessages"] = "toggleSupergroupJoinToSendMessages"
    supergroup_id: Int53
    join_to_send_messages: Bool
