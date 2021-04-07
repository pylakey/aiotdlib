# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AddChatMembers(BaseObject):
    """
    Adds multiple new members to a chat. Currently this method is only available for supergroups and channels. This method can't be used to join a chat. Members can't be added to a channel if it has more than 200 members
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        user_ids (:obj:`list[int]`)
            Identifiers of the users to be added to the chat. The maximum number of added users is 20 for supergroups and 100 for channels
        
    """

    ID: str = Field("addChatMembers", alias="@type")
    chat_id: int
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> AddChatMembers:
        return AddChatMembers.construct(**q)
