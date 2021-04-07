# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteMessages(BaseObject):
    """
    Deletes messages
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_ids (:obj:`list[int]`)
            Identifiers of the messages to be deleted
        
        revoke (:class:`bool`)
            Pass true to try to delete messages for all chat members. Always true for supergroups, channels and secret chats
        
    """

    ID: str = Field("deleteMessages", alias="@type")
    chat_id: int
    message_ids: list[int]
    revoke: bool

    @staticmethod
    def read(q: dict) -> DeleteMessages:
        return DeleteMessages.construct(**q)
