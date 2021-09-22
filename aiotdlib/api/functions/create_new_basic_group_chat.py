# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CreateNewBasicGroupChat(BaseObject):
    """
    Creates a new basic group and sends a corresponding messageBasicGroupChatCreate. Returns the newly created chat
    
    :param user_ids: Identifiers of users to be added to the basic group
    :type user_ids: :class:`list[int]`
    
    :param title: Title of the new basic group; 1-128 characters
    :type title: :class:`str`
    
    """

    ID: str = Field("createNewBasicGroupChat", alias="@type")
    user_ids: list[int]
    title: str = Field(..., min_length=1, max_length=128)

    @staticmethod
    def read(q: dict) -> CreateNewBasicGroupChat:
        return CreateNewBasicGroupChat.construct(**q)
