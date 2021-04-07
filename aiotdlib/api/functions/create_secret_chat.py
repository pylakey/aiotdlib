# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CreateSecretChat(BaseObject):
    """
    Returns an existing chat corresponding to a known secret chat
    
    Params:
        secret_chat_id (:class:`int`)
            Secret chat identifier
        
    """

    ID: str = Field("createSecretChat", alias="@type")
    secret_chat_id: int

    @staticmethod
    def read(q: dict) -> CreateSecretChat:
        return CreateSecretChat.construct(**q)
