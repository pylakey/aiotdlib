# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CreateSecretChat(BaseObject):
    """
    Returns an existing chat corresponding to a known secret chat
    
    :param secret_chat_id: Secret chat identifier
    :type secret_chat_id: :class:`int`
    
    """

    ID: str = Field("createSecretChat", alias="@type")
    secret_chat_id: int

    @staticmethod
    def read(q: dict) -> CreateSecretChat:
        return CreateSecretChat.construct(**q)
