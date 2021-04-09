# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CreateNewBasicGroupChat(BaseObject):
    """
    Creates a new basic group and sends a corresponding messageBasicGroupChatCreate. Returns the newly created chat
    
    Params:
        user_ids (:obj:`list[int]`)
            Identifiers of users to be added to the basic group
        
        title (:class:`str`)
            Title of the new basic group; 1-128 characters
        
    """

    ID: str = Field("createNewBasicGroupChat", alias="@type")
    user_ids: list[int]
    title: str = Field(..., min_length=1, max_length=128)

    @staticmethod
    def read(q: dict) -> CreateNewBasicGroupChat:
        return CreateNewBasicGroupChat.construct(**q)
