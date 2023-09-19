# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClickChatSponsoredMessage(BaseObject):
    """
    Informs TDLib that the user opened the sponsored chat via the button, the name, the photo, or a mention in the sponsored message

    :param chat_id: Chat identifier of the sponsored message
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the sponsored message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["clickChatSponsoredMessage"] = "clickChatSponsoredMessage"
    chat_id: Int53
    message_id: Int53
