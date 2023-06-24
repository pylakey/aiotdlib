# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetChatClientData(BaseObject):
    """
    Changes application-specific data associated with a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param client_data: New value of client_data
    :type client_data: :class:`String`
    """

    ID: typing.Literal["setChatClientData"] = "setChatClientData"
    chat_id: Int53
    client_data: String
