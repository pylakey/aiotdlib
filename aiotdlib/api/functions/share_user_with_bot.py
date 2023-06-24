# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ShareUserWithBot(BaseObject):
    """
    Shares a user after pressing a keyboardButtonTypeRequestUser button with the bot

    :param chat_id: Identifier of the chat with the bot
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message with the button
    :type message_id: :class:`Int53`
    :param button_id: Identifier of the button
    :type button_id: :class:`Int32`
    :param shared_user_id: Identifier of the shared user
    :type shared_user_id: :class:`Int53`
    :param only_check: Pass true to check that the user can be shared by the button instead of actually sharing them
    :type only_check: :class:`Bool`
    """

    ID: typing.Literal["shareUserWithBot"] = "shareUserWithBot"
    chat_id: Int53
    message_id: Int53
    button_id: Int32
    shared_user_id: Int53
    only_check: Bool = False
