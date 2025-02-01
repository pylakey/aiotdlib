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
    MessageSender,
)


class SetMessageSenderBotVerification(BaseObject):
    """
    Changes the verification status of a user or a chat by an owned bot

    :param bot_user_id: Identifier of the owned bot, which will verify the user or the chat
    :type bot_user_id: :class:`Int53`
    :param verified_id: Identifier of the user or the supergroup or channel chat, which will be verified by the bot
    :type verified_id: :class:`MessageSender`
    :param custom_description: Custom description of verification reason; 0-getOption("bot_verification_custom_description_length_max"). If empty, then "was verified by organization "organization_name"" will be used as description. Can be specified only if the bot is allowed to provide custom description
    :type custom_description: :class:`String`
    """

    ID: typing.Literal["setMessageSenderBotVerification"] = Field(
        "setMessageSenderBotVerification", validation_alias="@type", alias="@type"
    )
    bot_user_id: Int53
    verified_id: MessageSender
    custom_description: String = ""
