# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetLoginUrl(BaseObject):
    """
    Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl. Use the method getLoginUrlInfo to find whether a prior user confirmation is needed. If an error is returned, then the button must be handled as an ordinary URL button

    :param chat_id: Chat identifier of the message with the button
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier of the message with the button
    :type message_id: :class:`Int53`
    :param button_id: Button identifier
    :type button_id: :class:`Int53`
    :param allow_write_access: Pass true to allow the bot to send messages to the current user
    :type allow_write_access: :class:`Bool`
    """

    ID: typing.Literal["getLoginUrl"] = "getLoginUrl"
    chat_id: Int53
    message_id: Int53
    button_id: Int53
    allow_write_access: Bool = False
