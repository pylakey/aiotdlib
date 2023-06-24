# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetLoginUrlInfo(BaseObject):
    """
    Returns information about a button of type inlineKeyboardButtonTypeLoginUrl. The method needs to be called when the user presses the button

    :param chat_id: Chat identifier of the message with the button
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier of the message with the button
    :type message_id: :class:`Int53`
    :param button_id: Button identifier
    :type button_id: :class:`Int53`
    """

    ID: typing.Literal["getLoginUrlInfo"] = "getLoginUrlInfo"
    chat_id: Int53
    message_id: Int53
    button_id: Int53
