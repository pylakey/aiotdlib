# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CloseChat(BaseObject):
    """
    Informs TDLib that the chat is closed by the user. Many useful activities depend on the chat being opened or closed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["closeChat"] = "closeChat"
    chat_id: Int53
