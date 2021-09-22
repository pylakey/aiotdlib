# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CreateNewSecretChat(BaseObject):
    """
    Creates a new secret chat. Returns the newly created chat
    
    :param user_id: Identifier of the target user
    :type user_id: :class:`int`
    
    """

    ID: str = Field("createNewSecretChat", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> CreateNewSecretChat:
        return CreateNewSecretChat.construct(**q)
