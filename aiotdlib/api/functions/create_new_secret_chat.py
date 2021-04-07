# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CreateNewSecretChat(BaseObject):
    """
    Creates a new secret chat. Returns the newly created chat
    
    Params:
        user_id (:class:`int`)
            Identifier of the target user
        
    """

    ID: str = Field("createNewSecretChat", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> CreateNewSecretChat:
        return CreateNewSecretChat.construct(**q)
