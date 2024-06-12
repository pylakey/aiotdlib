# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReportChatSponsoredMessage(BaseObject):
    """
    Reports a sponsored message to Telegram moderators

    :param chat_id: Chat identifier of the sponsored message
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the sponsored message
    :type message_id: :class:`Int53`
    :param option_id: Option identifier chosen by the user; leave empty for the initial request
    :type option_id: :class:`Bytes`
    """

    ID: typing.Literal["reportChatSponsoredMessage"] = Field(
        "reportChatSponsoredMessage", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    message_id: Int53
    option_id: Bytes
