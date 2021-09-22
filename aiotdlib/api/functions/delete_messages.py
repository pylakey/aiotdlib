# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class DeleteMessages(BaseObject):
    """
    Deletes messages
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_ids: Identifiers of the messages to be deleted
    :type message_ids: :class:`list[int]`
    
    :param revoke: Pass true to try to delete messages for all chat members. Always true for supergroups, channels and secret chats
    :type revoke: :class:`bool`
    
    """

    ID: str = Field("deleteMessages", alias="@type")
    chat_id: int
    message_ids: list[int]
    revoke: bool

    @staticmethod
    def read(q: dict) -> DeleteMessages:
        return DeleteMessages.construct(**q)
