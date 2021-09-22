# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetSecretChat(BaseObject):
    """
    Returns information about a secret chat by its identifier. This is an offline request
    
    :param secret_chat_id: Secret chat identifier
    :type secret_chat_id: :class:`int`
    
    """

    ID: str = Field("getSecretChat", alias="@type")
    secret_chat_id: int

    @staticmethod
    def read(q: dict) -> GetSecretChat:
        return GetSecretChat.construct(**q)
