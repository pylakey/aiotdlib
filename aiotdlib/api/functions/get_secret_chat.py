# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetSecretChat(BaseObject):
    """
    Returns information about a secret chat by its identifier. This is an offline request
    
    Params:
        secret_chat_id (:class:`int`)
            Secret chat identifier
        
    """

    ID: str = Field("getSecretChat", alias="@type")
    secret_chat_id: int

    @staticmethod
    def read(q: dict) -> GetSecretChat:
        return GetSecretChat.construct(**q)
