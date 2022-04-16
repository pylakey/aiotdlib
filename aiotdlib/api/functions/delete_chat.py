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
    Deletes a chat along with all messages in the corresponding chat for all chat members. For group chats this will release the username and remove all members. Use the field chat.can_be_deleted_for_all_users to find whether the method can be applied to the chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("deleteChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> DeleteChat:
        return DeleteChat.construct(**q)
