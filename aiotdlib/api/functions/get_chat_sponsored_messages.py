# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetChatSponsoredMessages(BaseObject):
    """
    Returns sponsored messages to be shown in a chat; for channel chats only
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getChatSponsoredMessages", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChatSponsoredMessages:
        return GetChatSponsoredMessages.construct(**q)
