# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteChat(BaseObject):
    """
    Deletes a chat along with all messages in the corresponding chat for all chat members; requires owner privileges. For group chats this will release the username and remove all members. Chats with more than 1000 members can't be deleted using this method
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("deleteChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> DeleteChat:
        return DeleteChat.construct(**q)
