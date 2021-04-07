# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class UnpinAllChatMessages(BaseObject):
    """
    Removes all pinned messages from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat
        
    """

    ID: str = Field("unpinAllChatMessages", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> UnpinAllChatMessages:
        return UnpinAllChatMessages.construct(**q)
