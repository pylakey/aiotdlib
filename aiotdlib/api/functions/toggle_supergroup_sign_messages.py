# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleSupergroupSignMessages(BaseObject):
    """
    Toggles whether sender signature or link to the account is added to sent messages in a channel; requires can_change_info member right

    :param supergroup_id: Identifier of the channel
    :type supergroup_id: :class:`Int53`
    :param sign_messages: New value of sign_messages
    :type sign_messages: :class:`Bool`
    :param show_message_sender: New value of show_message_sender
    :type show_message_sender: :class:`Bool`
    """

    ID: typing.Literal["toggleSupergroupSignMessages"] = Field(
        "toggleSupergroupSignMessages", validation_alias="@type", alias="@type"
    )
    supergroup_id: Int53
    sign_messages: Bool
    show_message_sender: Bool
